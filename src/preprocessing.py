import re

def normalize_text(text: str) -> str:
    """Normalize whitespace without removing wording or punctuation evidence."""
    return re.sub(r"\s+"," ",str(text)).strip()

def prepare_texts(texts):
    return [normalize_text(t) for t in texts]
