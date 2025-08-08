def life_in_weeks(age):
    x = 90 * 52
    age = x - (age * 52)
    print(f"Assuming you'll live 90 years. You have {age} weeks left.")

age = int(input('Enter your age in years: '))
life_in_weeks(age)
