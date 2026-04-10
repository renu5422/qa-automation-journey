def is_anagram(str1, str2):
    if len(str1) != len(str2):
        return False

    count = {}

    for char in str1:
        count[char] = count.get(char, 0) + 1

    for char in str2:
        if char not in count:
            return False
        count[char] -= 1

    return all(value == 0 for value in count.values())

print(is_anagram("listen", "silent"))