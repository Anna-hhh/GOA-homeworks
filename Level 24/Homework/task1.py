word = input("შეიყვანეთ სიტყვა: ")


if word == word[::-1]:
    print("ეს სიტყვა განსაკუთრებულია (palindrome)!")
else:
    print("ეს ჩვეულებრივი სიტყვაა.")