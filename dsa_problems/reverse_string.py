def reverse_string(s: str) -> str:
    return s[::-1]


if __name__ == "__main__":
    assert reverse_string("hello") == "olleh"
    assert reverse_string("abc") == "cba"
    print(reverse_string("hello"))
