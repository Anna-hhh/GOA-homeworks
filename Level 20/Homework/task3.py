# 5) მომხმარებელს 3 მცდელობა აქვს სწორი PIN კოდის შეყვანისთვის. თუ შეიყვანს სწორად, დაიბეჭდება "Access Granted", სხვა შემთხვევაში "Access Denied" გამოიყენეთ პირობითი განცხადებები

correct_pin = "1234"
attempts = 3  

while attempts > 0:
    pin = input("შეიყვანეთ PIN კოდი: ")
    if pin == correct_pin:
        print("Access Granted")
        break
    else:
        attempts -= 1
        print(f"არასწორი PIN. დარჩენილი მცდელობები: {attempts}")

if attempts == 0:
    print("Access Denied")