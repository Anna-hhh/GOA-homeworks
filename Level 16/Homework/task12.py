# 13) შექმენით პროგრამა რომელიც მომხმარებელს შეეკითხება პაროლს სანამ ის არ შემოიყვანს goabest123-ს

 
password = input("password: ")
while password != "goabest123":
    print("not right password")
    password = input("password: ")
print("right password")