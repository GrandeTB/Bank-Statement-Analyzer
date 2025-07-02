import pdfplumber
import pandas as pd
import re
import os

def extract_operations_from_pdf(pdf_path, year):
    lines = []

    # Extract transaction-like lines from PDF
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            text = page.extract_text()
            if text:
                for line in text.split('\n'):
                    if re.match(r"\d{2}\.\d{2}\s+\d{2}\.\d{2}", line.strip()):
                        lines.append(line.strip())

    data = []
    for line in lines:
        parts = line.split()
        if len(parts) >= 5:
            date_val = parts[1]
            amount_str = parts[-1].replace(",", ".").replace("€", "")
            try:
                amount = float(amount_str)
            except ValueError:
                amount = None

            description = " ".join(parts[2:-1])
            data.append({
                "date": f"{date_val}.{year}",
                "description": description,
                "amount": -amount if amount else None  # treat all as debit
            })

    df = pd.DataFrame(data)
    df["date"] = pd.to_datetime(df["date"], format="%d.%m.%Y", errors="coerce")
    df = df.dropna(subset=["date", "amount"])
    return df

def process_all_pdfs(input_folder, output_folder, merged_csv_path, year):
    os.makedirs(output_folder, exist_ok=True)
    all_dfs = []

    for file in os.listdir(input_folder):
        if file.endswith(".pdf"):
            pdf_path = os.path.join(input_folder, file)
            base_name = os.path.splitext(file)[0]
            output_csv = os.path.join(output_folder, f"{base_name}_clean.csv")

            print(f"📄 Processing: {file}")
            df = extract_operations_from_pdf(pdf_path, year)
            df.to_csv(output_csv, index=False, encoding="utf-8-sig")
            all_dfs.append(df)

    # Merge all cleaned DataFrames into one
    if all_dfs:
        merged_df = pd.concat(all_dfs, ignore_index=True)
        merged_df.to_csv(merged_csv_path, index=False, encoding="utf-8-sig")
        print(f"\n✅ All PDFs processed and merged into: {merged_csv_path}")
    else:
        print("⚠️ No valid PDFs found.")

if __name__ == "__main__":
    input_folder = "data/raw_pdfs/"
    output_folder = "data/cleaned_data/"
    merged_csv_path = "data/all_statements_merged.csv"
    year = 2025  # Set your year here or detect it later

    process_all_pdfs(input_folder, output_folder, merged_csv_path, year)
