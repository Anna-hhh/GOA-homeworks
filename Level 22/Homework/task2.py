# 3) მომხმარებელს შემოატანინეთ რიცხვი 0-იდან 4-მდე და შეინახეთ ის "user_choice"-ის ცვლადში, შემდეგ ბოსტნეულსი სიიდან დაუბეჭდეთ ის ელემენტი რომელიც მომხმარებელმა აირჩია, ესეიგი იმ user_choice ინდექსზე მყოფი ელემენტი სიაში
 
   

user_choice = int(input("შეიყვანეთ რიცხვი 0-დან 4-მდე: "))
vegetables = ["carrot", "potato", "onion", "cabbage", "pepper"]
if 0 <= user_choice < len(vegetables):
    print("თქვენი არჩევანი არის:", vegetables[user_choice])
