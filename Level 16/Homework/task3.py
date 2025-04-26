# 4) for ციკლის საშვალებით გამოთვალეთ 20-იდან 100-მდე ყველა ლუწი რიცხვის ჯამი, საბოლოოდ დაბეჭდეთ შედეგი


for number in range(20, 101):
    if number % 2 == 0:
        total += number

print("Sum of even numbers from 20 to 100 is:", total)
