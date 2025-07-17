import re

def extract_clauses(text):
    text = re.sub(r'\s+', ' ', text)  # Normalize whitespace
    clauses = {}

    # Payment Terms
    payment = re.search(r'(Payment terms are .*?\.)', text, re.IGNORECASE)
    if payment:
        clauses['payment_terms'] = payment.group(1)

    # Termination Clause
    termination = re.search(r'(Either party may terminate .*?\.)', text, re.IGNORECASE)
    if termination:
        clauses['termination'] = termination.group(1)

    # Governing Law (optional pattern)
    governing_law = re.search(r'(This Agreement shall be governed .*?\.)', text, re.IGNORECASE)
    if governing_law:
        clauses['governing_law'] = governing_law.group(1)

    return clauses

def assess_risk(clauses):
    risky_phrases = ['terminate', 'penalty', 'non-compliance', 'breach', 'indemnify']
    risk_score = 0
    risky_clauses = []

    for label, clause in clauses.items():
        for word in risky_phrases:
            if word in clause.lower():
                risk_score += 1
                risky_clauses.append(label)
                break

    normalized_risk = round(risk_score / max(len(clauses), 1), 2)
    return {
        "risk_score": normalized_risk,
        "risky_clauses": risky_clauses
    }