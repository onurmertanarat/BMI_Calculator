user_name = input("Name: ")
user_age = input("Age: ")
user_height = int(input("Height (cm): "))
user_weight = int(input("Weight (kg): "))
user_bmi = 0


def bmi_calculate(height, weight):
    height = float(height)
    bmi = (weight / (pow((height/100), 2)))
    print(round(bmi, 1))


bmi_calculate(user_height, user_weight)
