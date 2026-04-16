import re


def is_valid_palindrome(s: str) -> bool:
    cleaned = re.sub(r"[^a-zA-Z0-9]", "", s).lower()
    return cleaned == cleaned[::-1]


if __name__ == "__main__":
    examples = [
        ("A man, a plan, a canal: Panama", True),
        ("race a car", False),
        ("", True),
        ("0P", False),
    ]

    for text, expected in examples:
        result = is_valid_palindrome(text)
        print(f"Input: {text!r} -> {result}")
        assert result == expected
    print("All tests passed.")