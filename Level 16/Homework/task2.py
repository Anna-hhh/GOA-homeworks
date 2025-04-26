# 3) for ციკლის საშვალებით გამოთვალეთ 10-იდან 50-ის ჩათვლით ყველა რიცხვის ჯამი

total = 0
for number in range(10, 51):  # 50 შედის დიაპაზონში
    total += number

print("Sum of numbers from 10 to 50 is:", total)