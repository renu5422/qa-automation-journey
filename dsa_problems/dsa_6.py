def word_frequency(sentence):
    words = sentence.split()
    freq = {}

    for word in words:
        freq[word] = freq.get(word, 0) + 1

    return freq


text = "playwright is powerful playwright is fast"
print(word_frequency(text))