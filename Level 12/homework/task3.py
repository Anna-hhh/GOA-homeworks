'''შექმენით 5 ცვლადი, რომლებშიც შეინახავთ განსხვავებულ ლოგიკურ და შედარების ოპერაციათა შედეგებს (უნდა იყოს შედარების და ლოგიკური ოპერატორები ერთად მაგალითად temperature > 30 and not cloudy), გვერდზე კომენტარის საშვალებით მიუწერეთ ეს შედეგი (boolean მნიშვნელობა) აიღეთ მრავალფეროვანი კომბინაციები'''


result1 = (10 > 5) and (3 < 7)  # True


result2 = (8 == 8) or (5 > 10)  # True:


result3 = not (4 <= 2)  # True


result4 = (15 != 10) and not (20 < 15)  # True


temperature = 35
cloudy = False
result5 = (temperature > 30) and not cloudy  # True