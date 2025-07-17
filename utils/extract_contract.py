import re

def extract_contract_data(text):
    data = {}

    # Normalize whitespace
    text = re.sub(r'\s+', ' ', text)

    # Extract parties (e.g., between AlphaTech Ltd. and BetaCorp Inc.)
    match = re.search(r'between\s+(.*?)\s+and\s+(.*?)[\.,]', text, re.IGNORECASE)
    data['parties'] = list(match.groups()) if match else "MISSING"

    # Extract effective date (e.g., effective as of January 1, 2024)
    effective_date = re.findall(r'effective\s+(?:as\s+of\s+)?([A-Za-z]+\s+\d{1,2},?\s*\d{0,4})', text, re.IGNORECASE)
    data['effective_date'] = effective_date if effective_date else "MISSING"

    # Extract termination or end date
    termination_date = re.findall(r'\b(?:to|until|terminate(?:s|d)?(?: on)?)\s+([A-Za-z]+\s+\d{1,2},?\s*\d{0,4})', text, re.IGNORECASE)
    data['termination_date'] = termination_date if termination_date else "MISSING"


    return data
