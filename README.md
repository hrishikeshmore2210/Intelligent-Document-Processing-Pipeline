# 📄 Intelligent Document Processing Pipeline (Contracts & Invoices)

An end-to-end Python and Streamlit-based system to process legal and financial documents like contracts and invoices using OCR, NLP, and intelligent clause analysis.

## 🚀 Features

- ✅ Upload scanned or digital PDFs
- 🧠 Automatically classify as `contract` or `invoice`
- 🔍 Extract key fields:
  - **Contracts**: Parties, effective/termination dates, clauses
  - **Invoices**: Vendor, dates, total amount
- 📊 Perform clause-based **risk analysis**
- 💻 Streamlit web UI with:
  - File upload
  - File history
  - Clause & risk summary
  - Reset confirmation
  - Downloadable JSON output

## 📸 Screenshots

| Upload UI | Extracted Output |
|-----------|------------------|
| ![Upload](screenshots/upload_view.png) | ![Results](screenshots/result_view.png) |

## 🛠️ Tech Stack

- Python 3.13
- Streamlit
- pytesseract + poppler (for OCR)
- regex, spaCy (for extraction)
- Git for version control

## 🔧 Setup Instructions

1. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

2. **Install OCR tools**
   - Tesseract: https://github.com/UB-Mannheim/tesseract/wiki
   - Poppler: https://github.com/oschwartz10612/poppler-windows/releases

3. **Run the app**
   ```bash
   streamlit run streamlit_app.py
   ```

4. **Upload a contract or invoice PDF and view results**

## 📂 Project Structure

```
idp_pipeline/
├── data/input_docs/           # Upload test files here
├── data/output_json/          # Output results
├── utils/                     # All extraction & logic modules
├── streamlit_app.py           # Streamlit UI
├── main.py                    # CLI pipeline (optional)
├── README.md
```

## 📃 Author

**Hrishikesh More**  
MSc in Artificial Intelligence  
National College of Ireland

## 📌 License

MIT License