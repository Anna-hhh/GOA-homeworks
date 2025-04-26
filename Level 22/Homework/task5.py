# 8) შექმენით სია 0-დან 15-მდე რიცხვებით. გამოიტანეთ მხოლოდ ის რიცხვები, რომლებიც კენტ ინდექსებზე დგანან

 
numbers = list(range(16))

for i in range(len(numbers)):
    if i % 2 != 0:
        print(numbers[i])
