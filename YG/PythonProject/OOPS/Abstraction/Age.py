from datetime import date

age = int(input("Enter your age: "))

current_year = date.today().year
birth_year = current_year - age

print("Your date of birth year is:", birth_year)


