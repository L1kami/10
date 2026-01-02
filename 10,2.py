import re

def first_word(text: str) -> str:
    match = re.search(r"[a-zA-Z']+", text)
    return match.group(0) if match else ""