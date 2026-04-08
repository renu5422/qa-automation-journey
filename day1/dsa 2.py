text = "automation"

vowels = "aeiou"
count = 0

for char in text:
    if char.lower() in vowels:
        count += 1

print("Vowel count:", count)