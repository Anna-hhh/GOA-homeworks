'''2) მომხმარებელს შემოატანინეთ თავისი სიმაღლე,
 შემდეგ შემოატანინეთ წლების რაოდენობა, მიღებული 
 ინფორმაცია შეინახეთ ცვლადში და გამოუთვალეთ მომხმარებელს
სავაურდო სიმაღლე იმ წლების შემდეგ რაც მან შემოიტანა თუ 
დაუშვათ ყოველ წელს სიმაღლე იზრდება 0.5-ით'''

height = float(input("Enter your height: "))
age = int(input("Enter your age: "))
height += age*0.5
print(height)