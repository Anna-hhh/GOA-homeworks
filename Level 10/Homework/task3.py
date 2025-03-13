'''აიღეთ 3 ცვლადი, შეინახეთ განსხავებული მონაცემთა ტიპები (str,int,float), შემდეგ type ინსტრუქციის გამოყენებით შეამოწმეთ, თუ რომელ მონაცემთა ტიპს ინახავს ცვლადი.'''

# String ტიპი
name = "გიორგი"  # str

# Integer ტიპი
age = 25  # int

# Float ტიპი
height = 1.75  # float

name_type = type(name)
age_type = type(age)
height_type = type(height)

print("name ცვლადის ტიპი არის:", name_type)
print("age ცვლადის ტიპი არის:", age_type)
print("height ცვლადის ტიპი არის:", height_type)