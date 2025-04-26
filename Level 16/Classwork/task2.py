''' მომხმარებელს შემოატანინეთ 2 რიცხვი, შემდეგ კი პირველი რიცხვიდან მეორეს ჩათვლით არსებული ყველა რიცხვი დაბეჭდეთ'''

num1 = int(input("write first number: "))
num2 = int(input("write second number: "))

for num in range(num1, num2 + 1):
    print(num)