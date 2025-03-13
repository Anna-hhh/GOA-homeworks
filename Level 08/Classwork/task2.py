'''
2) მომხმარებელს input-ის საშვალებით შემოტანინეთ ორი რიცხვი number1 და number2 შემდეგ კი
 დაბეჭდეთ მათი ჯამი. ასევე შექმენით level-ის ცვლადი რომელშიც მომხამრებელს შემოაყვანინებთ 
 მათ ამჟამინდელ level-ს, შეეცადეთ level-ის
 მნიშვნელობას დაუმატოთ ერთი და ისე დაბეჭდოთ. მიღებული
   შედეგებით გამოიტანეთ დასკვნა და დაწერეთ კომენტარებით
'''

num1 = input("enter number one: ")
num2 = input("enter number two?1")
print("the sum of the numbers is", num1 + num2)
level = input("your current lvl: ")
print("your lvl increased by 1", level + 1)

