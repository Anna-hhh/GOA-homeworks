'''შექმენით პროგრამა რომელიც მოხმარებელს შეეკითხება პაროლს სანამ სწორად არ ჩაწერს'''
right_password = "1234"

attempts = 0

while True:
    password = input("enter your password: ")
    if password == right_password:
        attempts += 1 
        print("right password")
        print("you tried", attempts, "times")
        break
    else:
        print("wrong password")