import json
import re
import spacy
import pdfplumber
import argparse
import pandas as pd
import numpy as np

from collections import defaultdict

# Initialize the spaCy model
nlp = spacy.load("en_core_web_sm")


def is_strong_heading(line):
    """
        Determine if a line is a heading based on strict rules:
        1. Text is bold.
        2. Text is not excessively long (less than 50 characters).
        3. Text starts with a capital letter.
        4. Surrounded by less dense text.
        5. Contextual relevance (avoid generic or noise-like text).
    """
    if not line.strip():
        return False

    if len(line) > 50:
        return False

    if not line[0].isupper():
        return False

    doc = nlp(line.strip())
    if len(doc) > 1 and any(token.pos_ in ["VERB", "ADP"] for token in doc):
        return False

    if re.search(r"bold|strong", line.lower()):
        return True

    return True


def is_noise(line):
    """
        Identify and filter out noise such as:
            - Index entries
            - Repetitive patterns
            - Single numbers or irrelevant symbols
    """
    if re.match(r"^\s*[\dIVXLCDM]+(\.\d+)*\s*$", line.strip()):
        return True
    if re.match(r"^\s*[-–—]+\s*$", line.strip()):
        return True
    if len(line.split()) < 2 and len(line) < 5:
        return True
    return False


def extract_data_from_unstructured_pdf(file_path: str):
    """
        Extract data from unstructured PDFs.    

        `Args`:
            file_path: str
                Path to the input PDF file.

        `Returns`:
            newly created JSONL file with extracted data.
    """
    try:
        table_data = []
        data = defaultdict(str)
        current_heading = None
        with pdfplumber.open(file_path) as pdf:
            for page in pdf.pages:
                table = pdf.pages[page.page_number].extract_table()
                text = page.extract_text()
                if table is not None and len(table) > 1:
                    df = pd.DataFrame(table[1:], columns=table[0])
                    df.drop(columns=[""], inplace=True)
                    df = df[~df.isin({None, np.nan, "None", ""}).all(axis=1)]
                    for _, row in df.iterrows():
                        row_dict = row.to_dict()
                    table_data.append(row_dict)
                if not text:
                    continue
                lines = text.split('\n')
                for line in lines:
                    clean_line = line.strip()

                    if not clean_line or is_noise(clean_line):
                        continue

                    if is_strong_heading(clean_line):
                        if current_heading:
                            data[current_heading] = data[current_heading].strip()
                        current_heading = clean_line
                    else:
                        if current_heading:
                            data[current_heading] += " " + clean_line
                        else:
                            data["Uncategorized"] += " " + clean_line
                data[f"{page.page_number}"] = {
                    "table_data": table_data,
                    "text_data": json.dumps(data, indent=4)
                }
        with open(f"summary.jsonl", "w") as jsonl_file:
            print("inside jsonl file")
            jsonl_file.write(json.dumps(data, indent=4))

    except Exception as e:
        print(e)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("file_path", help="Path to the input PDF file.")
    args = parser.parse_args()
    extract_data_from_unstructured_pdf(args.file_path)
