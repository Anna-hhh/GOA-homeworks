start = int(input("შეიყვანეთ დაწყების რიცხვი: "))
end = int(input("შეიყვანეთ დასრულების რიცხვი: "))

if end < start:
    print("არასწორი შუალედი")
else:
    total = 0
    for num in range(start, end + 1):
        print(num)
        total += num
    print("ჯამი:", total)