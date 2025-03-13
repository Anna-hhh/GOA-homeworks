'''
შექმენით 5 ცვლადი რომლებშიც 
შეინახავთ წიგნების თავდაპირველ ფასს, შემდეგ 
შექმენით ცვლადი რომელშიც შეინახავთ ფასდაკლების 
ოდენობას, შექმენით ახალი ფასის მქონე წიგნების ცვლადები,
რომელთა მნიშვნელობა იქნება ძველ მნიშვნელობას 
გამოკლებული ახალი, საბოლოოდ კი დაბეჭდეთ ახალი
წიგნების ფასები (გამოიყენეთ კარგი მიდგომები: რომ 
ცვლადის მნიშვნელობის მინიჭებისას შეგიძლიათ სხვა 
ცვლადის გამოყენება, კოდი ახსენით კომენტარების საშვალებით,
ცვლადებს დაარქვით აღმწერი სახელები snake_case-ის სტილში)
'''
# წიგნების ფასები
book1= 10
book2= 20
book3= 30
book4= 40
book5= 50

# ფასდაკლებები
discount= 5

# ახალი ფასები
new_book1= book1 - discount
new_book2= book2 - discount
new_book3= book3 - discount
new_book4= book4 - discount
new_book5= book5 - discount

# დაბეჭდეთ ახალი ფასები
print("new price for book 1:", new_book1)
print("new price for book 2:", new_book2)
print("new price for book 3:", new_book3)
print("new price for book 4:", new_book4)
print("new price for book 5:", new_book5)