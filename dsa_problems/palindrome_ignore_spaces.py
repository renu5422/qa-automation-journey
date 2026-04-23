def is_palindrome(s: str) -> bool:
    normalized = s.replace(" ", "").lower()
    return normalized == normalized[::-1]


if __name__ == "__main__":
    assert is_palindrome("racecar") is True
    assert is_palindrome("hello") is False
    print(is_palindrome("racecar"))
