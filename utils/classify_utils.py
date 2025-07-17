def classify_document(text):
    text = text.lower()
    
    contract_keywords = [
        "agreement", "between", "effective as of", "terminate", "witness", "hereby", "obligations", "party", "governing law"
    ]
    
    invoice_keywords = [
        "invoice", "amount due", "bill to", "due date", "invoice number", "total", "from:", "to:", "description", "quantity", "price"
    ]
    
    contract_score = sum(1 for kw in contract_keywords if kw in text)
    invoice_score = sum(1 for kw in invoice_keywords if kw in text)

    if contract_score > invoice_score:
        return "contract"
    elif invoice_score > contract_score:
        return "invoice"
    elif contract_score == invoice_score and contract_score > 0:
        return "ambiguous"
    else:
        return "unknown"
