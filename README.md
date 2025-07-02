# 🧾 Bank Statement Analyzer

**Bank Statement Analyzer** is a lightweight Python tool that extracts tables from bank statement PDFs, cleans the data, and classifies transactions for further analysis or visualization (e.g., in Power BI or Excel).

---

## 🚀 Features

- 📄 Extracts structured tables from PDF bank statements using `pdfplumber`
- 🧹 Cleans, formats, and normalizes dates, amounts, and descriptions
- 🏷️ Automatically categorizes transactions (e.g., Rent, Groceries, Income)
- 📊 Outputs clean CSV files ready for analysis or dashboarding

---

## 🧰 Requirements

- Python 3.8 or higher

Python packages:

- `pdfplumber`
- `pandas`

Install dependencies with:

```bash
pip install -r requirements.txt
