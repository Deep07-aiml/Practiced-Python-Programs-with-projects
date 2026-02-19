#Day2 of 100 days of python

# Primitive Datatype 
# String 
print("Hello"[0])  #Pulling of individual character is known as Subscript method.
print("Hello"[4])  #output:- 'o' "123" is also a string not number.
print("123" + "345") #Everything written inside a double quote is a string.
print("Hello" + " world")

#Integer 
print(123 + 345)

#For Large Number we use 'commas' inbetween to represent it here in python we use '_' (underscore)
# 123_456_789

#Float
# 3.14159 Decimal point (Floating point Number)

#Boolean

# True 
# False

print(len('5678'))

num_char = len(input("What is your name? "))
#print("Your name has" + num_char + " characters.")  TypeError Can't concate 'int' 
new_num_char = str(num_char) # Type Conversion

#Type Checking or Type Casting 
print(type(num_char)) #Use type() to check it's Datatype --> <class 'int'>

print("Your name has " + new_num_char + " characters.")

a = int(123)
print(type(a))  # Type integer

b = float(345)
print(type(b))  # Type float

print( 70 + float("100.5"))

print(str(70) + str(100))

# Challenge of Day 2

two_digit_number = input("Type a two digit number: ")

# Get the first and second digits using subscripting then convert string to int.
first_digit = int( two_digit_number[0])
second_digit = int(two_digit_number[1])

#Add the two digits together
result = (first_digit + second_digit)
print(result)

#PEMDASLT
# Paranthesis , exponents , Multiplication , Division , Addition , Subtraction , left to right
#  ()
# **
# * /
# + -

print(3 * 3 + 3 / 3 - 3)

# BMI Calculator Challenge

height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))

# print(type(height))
# print(type(weight))

BMI = int((weight) / (height * height))
print(BMI)

# Rounding a number 

print(8/3) # 2.6666666 floating point number
#Coversion from float to integer
print(int(8/3)) # to round the number use 'round' function. chopoff the decimal numbers to get whole number

print(round(8/3)) # O/P:- 3 used 'round' function to roundoff decimal number.
print(round(8/3,2)) # Precision round to two decimal places. O/P :- 2.67
print(round(8/3,3))
print(round(2.6666,3)) # 2.667 precision to 3 decimal round number.  O/P :- 2.667

#Don't need to convert into integer in floor division
print(8//3) #floor division(gives integer as datatype) can be used without converting into integer 

print(type(8/3)) # float datatype
print(type(8//3)) # integer datatype

result = 4/2
result /= 2
print(result)

score = 0
# new_score += 1  #(shorthand operator)
height = 1.8
isWinning = True

# f-string :- use to stop TypeError concate str ('not int') to str
print(f"your score is {score}, your height is {height}, you are winning is {isWinning}")

# Challenge 
age = int(input("What is your current age? "))
years = 90 - age
Days = years * 365
weeks = years * 52
months = years * 12
print(f"You have {Days}, {weeks} weeks and {months} months left.")
