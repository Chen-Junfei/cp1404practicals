"""
Word Occurrences
Estimate: 10 minutes
Actual:   16 minutes
"""

test = str(input("Test: "))
words = test.lower().split(" ")
words_to_count = {}

for word in words:
    if word in words_to_count:
        words_to_count[word] += 1
    else:
        words_to_count[word] = 1

word_width = len(max(list(words_to_count.keys()), key=len))

for word in dict(sorted(words_to_count.items())):
    print(f"{word:<{word_width}}: {words_to_count[word]}")
