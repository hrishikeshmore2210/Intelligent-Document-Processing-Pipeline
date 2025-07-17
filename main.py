from utils.ocr_utils import pdf_to_text
from utils.classify_utils import classify_document
from utils.extract_invoice import extract_invoice_data
from utils.extract_contract import extract_contract_data
from utils.validate_utils import validate_data
from utils.extract_clauses import extract_clauses, assess_risk
import os, json

INPUT_DIR = "data/input_docs/"
OUTPUT_DIR = "data/output_json/"

def process_document(filename):
    full_path = os.path.join(INPUT_DIR, filename)
    text = pdf_to_text(full_path)
    doc_type = classify_document(text)

    if doc_type == "invoice":
        raw_data = extract_invoice_data(text)
    elif doc_type == "contract":
        raw_data = extract_contract_data(text)

        # Extract intelligent clauses
        clauses = extract_clauses(text)
        risk = assess_risk(clauses)

        raw_data["clauses"] = clauses
        raw_data["risk_analysis"] = risk
    else:
        raw_data = {"error": "Unknown document type"}

    validated = validate_data(raw_data)

    output_file = os.path.join(OUTPUT_DIR, filename.replace(".pdf", ".json"))
    with open(output_file, "w") as f:
        json.dump(validated, f, indent=4)

    print(f"{filename} → {doc_type} → Saved to {output_file}")

if __name__ == "__main__":
    for file in os.listdir(INPUT_DIR):
        if file.endswith(".pdf"):
            process_document(file)