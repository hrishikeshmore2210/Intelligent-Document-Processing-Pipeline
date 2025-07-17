import re

def extract_invoice_data(text):
    data = {}
    data['vendor'] = re.findall(r'(?i)From:\s*(.*)', text)
    data['invoice_date'] = re.findall(r'(?i)Date:\s*(.*)', text)
    data['total_amount'] = re.findall(r'(?i)(Total|Amount Due):\s*\$?([\d,]+\.\d{2})', text)
    return data
