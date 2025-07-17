def validate_data(data_dict):
    validated = {}
    for k, v in data_dict.items():
        validated[k] = v if v else "MISSING"
    return validated
