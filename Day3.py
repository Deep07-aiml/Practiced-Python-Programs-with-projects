# Control flow with if_else
# Comparison operator :- ==, > , >= , < , <= , !=
print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))


if height >= 120:
    print("Can ride")
else:
    print("Can't ride sorry!")

# odd or Even exercise
number = int(input("Which numer do you want to check: "))

if number % 2 == 0 :
    print("This is an even number.")
else :
    print("This is an odd number.")

# Nested if-else
if height >= 120:
    print("You can ride the rollercoaster")
    age = int(input("enter your age: "))
    if age <= 18:
        print("$7")
    else:
        print("$12")
else:
    print("Can't ride sorry!")

# if / elif / else used to check multiple condition

if height >= 120:
    print("You can ride the rollercoaster")
    age = int(input("enter your age: "))
    if age < 12:
        print("pay $5.")
    elif age <= 18:
        print("Pay $7.")
    else:
        print("Pay $12.")
else:
    print("Can't ride sorry!")

# Challenge BMI calculator 2.0

height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
Bmi = round(weight / height**2)

if Bmi < 18.5:  # Check this condition first if it fails, then go to check next elif condition and so on.
    print(f"your bmi is {Bmi} and you are underweight.")
elif Bmi < 25 :
    print(f"Your bmi is {Bmi} and you are normal weight.")
elif Bmi < 30 :
    print(f"Your bmi is {Bmi} and you are overweight.")
elif Bmi < 35 :
    print(f"Your bmi is {Bmi} and you are obese.")
else :
    print(f"Your bmi is {Bmi} and you are clinically obese.")


# Challenge Leap year 
# Leap Year Rules
# - A year is a leap year if it is divisible by 4.
# - But if the year is also divisible by 100, then it is not a leap year
# - However, if the year is divisible by 400, then it is a leap year.

print("Leap year Tracker!! ")
year = int(input("Enter year here: "))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("Leap year")
        else:
            print("Not a Leap year!!")
    else:
        print("Leap year")
else:
    print("Not a Leap year!!")



print("Welcome to the Rollercoaster!!")
height = int(input("What is your height in cm? "))

if height >= 120:
    print("You can ride the rollercoaster")
    age = int(input("enter your age: "))
    if age < 12:
        bill = 5
        print("Child tickets $5.")
    elif age <= 18:
        bill = 7
        print("Youth tickets $7.")
    else:
        bill = 12
        print("Adult tickets $12.") 

    wants_photo = input("Do you want a photo taken? Y or N: ")
    if wants_photo == "Y":
        bill = bill + 3
    print(f"Your final bill is {bill}.")
else:
    print("Can't ride sorry!")

# Challenge Pizza Order

print("Welcome to Dominos")
size = input("What size pizza do you want? S, M or L: ")
add_pepperoni = input("Do you want pepproni? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")
bill = 0

if size == "S":
    bill = bill + 15
elif size == "M":
    bill = bill + 20
else:
    bill = bill + 25

if add_pepperoni == "Y":
    if size == "S":
        bill = bill + 2
    else :
        bill += 3

if extra_cheese == "Y":
        bill += 1
print(f"Your final bill is ${bill}")

# Logical Operator :- Combining multiple condition
# and, or, not

print("Welcome to the Rollercoaster!!")
height = int(input("What is your height in cm? "))
bill = 0

if height >= 120:
    print("You can ride the rollercoaster")
    age = int(input("enter your age: "))
    if age < 12:
        bill = 5
        print("Child tickets $5.")
    elif age <= 18:
        bill = 7
        print("Youth tickets $7.")
    elif age >=45 and age <= 56:
        print("Everything is going to be ok.HAVE A FREE RIDE ON US.")
    else:
        bill = 12
        print("Adult tickets $12.") 
    wants_photo = input("Do you want a photo taken? Y or N: ")
    if wants_photo == "Y":
        bill = bill + 3
    print(f"Your final bill is {bill}.")
else:
    print("Can't ride sorry!")

# Challenge L - calculator

name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
combined_string = name1 + name2
lower_case_string = combined_string.lower()

t = lower_case_string.count("t")
r = lower_case_string.count("r")
u = lower_case_string.count("u")
e = lower_case_string.count("e")

l = lower_case_string.count("l")
o = lower_case_string.count("o")
v = lower_case_string.count("v")
e = lower_case_string.count("e")

true = t + r + u + e
love = l + o + v + e

score = int(str(true)+ str(love)) #string cannot be compared so conversion is needed.

if (score < 10) or (score > 90):
    print(f"Your score is {score}, you go together like coke and mentos")
elif (score >= 40) and (score <= 50):
    print(f"Your score is {score}, you are alright together.")
else:
    print(f"Your score is {score}")


