def is_anagram(s, t):
    if len(s) != len(t):
        return False

    char_count = {}

    for char in s:
        char_count[char] = char_count.get(char, 0) + 1

    for char in t:
        if char not in char_count:
            return False

        char_count[char] -= 1

        if char_count[char] < 0:
            return False

    return True


if __name__ == "__main__":
    assert is_anagram("listen", "silent") is True
    assert is_anagram("hello", "bello") is False
    print(is_anagram("listen", "silent"))