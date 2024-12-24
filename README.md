# Financial Data Extraction

## Overview
`financial_data_extraction` is a Python-based project designed to extract, process, and analyze financial data from PDF documents. The project provides tools to parse financial information efficiently and output it into a structured format, such as JSONL.


## Table of Contents

- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Folder Structure](#folder-structure)
- [Usage](#usage)
- [Output Location](#output-location)
- [Reference](#references)

## Features
- Extract financial data from PDF documents.
- Process extracted data into a structured format (JSONL).
- Easy-to-use Jupyter Notebook for workflow demonstration and testing.

## Requirements
- Python 3.10.11 or higher

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/financial_data_extraction.git
   cd financial_data_extraction
   ```
2. Install required libraries:
    ```
    pip install -r requirements.txt
    ```

3. Verify that you have Python 3.10.11 installed:
    ```
    python --version
    ```

## Folder Structure
    financial_data_extraction/
    ├── jsonl/ # Folder to store the extracted table data in JSONL format.
    ├── pdfs/ # Folder to store the PDF files for processing.
    ├── .gitignore
    ├── pdf_summary.jsonl # Summary data extracted from respected PDF file
    ├── pdf_data.ipynb # Jupyter Notebook for processing PDF data.
    ├── README.md # Project documentation.
    └── requirements.txt # Project dependencies.

## Usage

1. Place the PDF files you want to process in the pdfs/ folder.
2. Open the pdf_data.ipynb file in Jupyter Notebook
3. Run the notebook cells to process the PDF files and extract financial data.
4. The processed data will be saved in the jsonl/ folder.

## Output Location
1. There are two files 
    1. extract_data.py which have script to generate all the combined data with table and summary.
        1. summary.jsonl file will be created.
    2. pdf_data.ipynb which have 2 functions which creates table data and summary data.
        1. You can find pdf_summary.jsonl for summary and extracted_data.jsonl under jsonl folder for table extraction.
2. Running Code
    1. For ipynb file just run any cell and you will get output.
    2. For .py file you need to set command from CLI
        ```
        - python file_name pdf_file_location
        - e.g extract_data.py pdfs/3M_2015_10K.pdf
        ```

## References
1. One can refer the output summary json from here - https://github.com/tejaspatel-atc/financial_data_extraction/blob/main/pdf_summary.jsonl