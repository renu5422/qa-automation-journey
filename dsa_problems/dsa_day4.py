def are_anagrams(first: str, second: str) -> bool:
    return sorted(first.replace(" ", "").lower()) == sorted(second.replace(" ", "").lower())


if __name__ == "__main__":
    assert are_anagrams("listen", "silent") is True
    assert are_anagrams("hello", "world") is False
    print(are_anagrams("listen", "silent"))
