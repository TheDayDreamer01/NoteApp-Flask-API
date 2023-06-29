import re


def is_valid_email(text : str) -> bool:
    pattern : str = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return re.match(pattern, text) is not None


