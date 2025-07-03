<p align="center">
  <img src="assets/banner.png" alt="Bank Statement Analyzer Banner" />
</p>

# 🧾 Bank Statement Analyzer

A lightweight Python tool to extract transactions from bank statement PDFs, clean and structure the data, and prepare it for analysis or visualization (e.g., with Power BI or Excel).

[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
![Python](https://img.shields.io/badge/python-3.10%2B-blue)

---

## 🚀 Features

- Extracts transaction lines from text-based PDF statements
- Cleans and normalizes dates, amounts, and descriptions
- Converts messy lines into structured CSV format
- Merges multiple statement files into a single dataset

---

## 📂 Project Structure

Bank-Statement-Analyzer/
├── assets/
├── data/
│ ├── raw_pdfs/
│ ├── cleaned_data/
│ ├── extracted_csvs/
│ └── all_statements_merged.csv
├── scripts/
│ └── process_bank_statement.py
├── .gitignore
├── requirements.txt
└── README.md

---

## 🛠️ Usage

1. Place your bank PDFs into `data/raw_pdfs/`
2. Run the script:
python scripts/process_bank_statement.py
3. Outputs:
Cleaned monthly CSVs → data/cleaned_data/
Merged CSV for analysis → data/all_statements_merged.csv

---

## 📊 Sample Output
date	description	amount
2025-05-06	CARTE 1234 AMAZON.FR	-32.90
2025-05-07	VIREMENT SALAIRE	1500.00
2025-05-08	ABONNEMENT NETFLIX	-13.49

---

## 📦 Requirements
Python 3.10+
pdfplumber
pandas

---

Install dependencies with:
pip install -r requirements.txt

Thanks for reading, next goal is to do a flask server and a SQLite Database to upload, extract, keep track, host locally a powerbi
