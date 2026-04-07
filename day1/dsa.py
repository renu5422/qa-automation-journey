# Reverse string
text = "hello"
print("Reversed:", text[::-1])

# Palindrome check
word = "madam"

if word == word[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")