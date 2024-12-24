# Financial Data Extraction

## Overview
`financial_data_extraction` is a Python-based project designed to extract, process, and analyze financial data from PDF documents. The project provides tools to parse financial information efficiently and output it into a structured format, such as JSONL.


## Table of Contents

- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Folder Structure](#folder-structure)
- [Usage](#usage)


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
1. After proceed with usage steps, you will find pdf_summary.jsonl for summary and extracted_data.jsonl under jsonl folder for table extraction.