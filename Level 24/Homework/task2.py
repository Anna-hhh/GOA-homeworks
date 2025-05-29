words = ["apple", "banana", "cherry", "date", "fig", "grape", "kiwi"]

reversed_words = words[::-1]

index = 0
for word in reversed_words:
    if index % 2 == 1: 
        print(word)
    index += 1