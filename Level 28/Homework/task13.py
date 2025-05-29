main_text = "Python is fun and powerful"
search_word = input("საძიებელი სიტყვა: ")
pos = main_text.find(search_word)
if pos != -1:
    print(pos)
else:
    print("word not found")