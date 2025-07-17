import streamlit as st
import os
import json
import tempfile
from utils.ocr_utils import pdf_to_text
from utils.classify_utils import classify_document
from utils.extract_invoice import extract_invoice_data
from utils.extract_contract import extract_contract_data
from utils.extract_clauses import extract_clauses, assess_risk
from utils.validate_utils import validate_data

# Set up Streamlit page
st.set_page_config(page_title="Intelligent Document Processor", layout="wide")
st.title("📄 Intelligent Document Processor (Contracts & Invoices)")

# Initialize session state for file history
if "history" not in st.session_state:
    st.session_state["history"] = []
if "result" not in st.session_state:
    st.session_state["result"] = None

# Upload PDF
uploaded_file = st.file_uploader("Upload a Contract or Invoice (PDF)", type=["pdf"])

# Process file
if uploaded_file:
    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as temp_file:
        temp_file.write(uploaded_file.read())
        temp_path = temp_file.name

    # OCR and Classification
    with st.spinner("🔍 Processing document..."):
        text = pdf_to_text(temp_path)
        doc_type = classify_document(text)
        result = {"document_type": doc_type}

        if doc_type == "invoice":
            extracted = extract_invoice_data(text)
        elif doc_type == "contract":
            extracted = extract_contract_data(text)
            clauses = extract_clauses(text)
            risk = assess_risk(clauses)
            extracted["clauses"] = clauses
            extracted["risk_analysis"] = risk
        else:
            extracted = {"error": "Could not classify document"}

        validated = validate_data(extracted)
        result["extracted_data"] = validated
        st.session_state["result"] = result
        st.session_state["history"].append(uploaded_file.name)

# Show result
if st.session_state["result"]:
    result = st.session_state["result"]
    st.success(f"✅ Document classified as: **{result['document_type'].upper()}**")

    # Summary paragraph for contract risk
    if result["document_type"] == "contract" and "risk_analysis" in result["extracted_data"]:
        risk = result["extracted_data"]["risk_analysis"]
        clauses = result["extracted_data"].get("clauses", {})
        clause_names = ", ".join(clauses.keys())
        summary = f"""
        This contract includes the following clauses: **{clause_names}**. 
        Based on automated clause analysis, the document carries a **risk score of {risk['risk_score']}**, 
        triggered primarily by: **{", ".join(risk['risky_clauses'])}**.
        """
        st.markdown("### 🧠 Clause & Risk Summary")
        st.markdown(summary)

    # Show extracted data
    st.subheader("🔍 Extracted Data")
    st.json(result, expanded=True)

    # Download button
    st.download_button(
        label="📥 Download Extracted JSON",
        data=json.dumps(result, indent=4),
        file_name="extracted_output.json",
        mime="application/json"
    )

# Show upload history
if st.session_state["history"]:
    st.sidebar.markdown("### 📁 File Upload History")
    for f in st.session_state["history"]:
        st.sidebar.write(f)

# Reset/clear button
if st.button("🔄 Reset"):
    st.session_state["result"] = None
    st.session_state["history"] = []
    st.rerun()

