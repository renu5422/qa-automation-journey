def first_non_repeating(s):
    char_count = {}

    # Step 1: Count frequency
    for char in s:
        char_count[char] = char_count.get(char, 0) + 1

    # Step 2: Find first unique
    for char in s:
        if char_count[char] == 1:
            return char

    return None


print(first_non_repeating("automation"))  