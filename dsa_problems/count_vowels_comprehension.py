def count_vowels(s: str) -> int:
    return sum(1 for char in s.lower() if char in "aeiou")


if __name__ == "__main__":
    assert count_vowels("automation") == 5
    assert count_vowels("bcdfg") == 0
    print(count_vowels("automation"))
