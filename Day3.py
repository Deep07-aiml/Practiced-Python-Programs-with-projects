# Control flow with if_else
# Comparison operator :- ==, > , >= , < , <= , !=
# print("Welcome to the rollercoaster!")
# height = int(input("What is your height in cm? "))


# if height >= 120:
#     print("Can ride")
# else:
#     print("Can't ride sorry!")

# odd or Even exercise
# number = int(input("Which numer do you want to check: "))

# if number % 2 == 0 :
#     print("This is an even number.")
# else :
#     print("This is an odd number.")

# Nested if-else
# if height >= 120:
#     print("You can ride the rollercoaster")
#     age = int(input("enter your age: "))
#     if age <= 18:
#         print("$7")
#     else:
#         print("$12")
# else:
#     print("Can't ride sorry!")

# if / elif / else used to check multiple condition

# if height >= 120:
#     print("You can ride the rollercoaster")
#     age = int(input("enter your age: "))
#     if age < 12:
#         print("pay $5.")
#     elif age <= 18:
#         print("Pay $7.")
#     else:
#         print("Pay $12.")
# else:
#     print("Can't ride sorry!")

# Challenge BMI calculator
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
Bmi = round(weight / height**2)

if Bmi >= 18.5:
    print("you are underweight.")
elif Bmi < 25 :
    print("You are normal weight.")
elif Bmi < 30 :
    print("You are overweight.")
elif Bmi < 35 :
    print("You are obese.")
else :
    print("You are clinically obese.")


