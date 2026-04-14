import re
from typing import List


def normalize_text(text: str) -> str:
    return re.sub(r"\s+", " ", text).strip().lower()


def extract_links(text: str) -> List[str]:
    return re.findall(r"https?://\S+", text)
