# #Day2 


# # Primitive Datatype 
# # String 
# print("Hello"[0])  #Pulling of individual character is known as Subscript method.
# print("Hello"[4])  #output:- 'o' "123" is also a string not number.
# print("123" + "345") #Everything written inside a double quote is a string.
# print("Hello" + " world")

# #Integer 
# print(123 + 345)

# #For Large Number we use 'commas' inbetween to represent it we use '_' (underscore)
# # 123_456_789

# #Float
# # 3.14159 Decimal point (Floating point Number)

# #Boolean

# # True 
# # False

# print(len('5678'))

# num_char = len(input("What is your name? "))
# #print("Your name has" + num_char + " characters.")  TypeError Can't concate 'int' 
# new_num_char = str(num_char) # Type COnversion

# #Type Checking or Type Casting
# print(type(num_char)) #Use type() to check it's type --> <class 'int'>

# print("Your name has " + new_num_char + " characters.")

# a = int(123)
# print(type(a))  # Type integer

# b = float(345)
# print(type(b))  # Type float

# print( 70 + float("100.5"))

# print(str(70) + str(100))

# # Challenge of Day 2

# two_digit_number = input("Type a two digit number: ")

# # Get the first and second digits using subscripting then convert string to int.
# first_digit = int( two_digit_number[0])
# second_digit = int(two_digit_number[1])

# #Add the two digits together
# result = (first_digit + second_digit)
# print(result)

# #PEMDASLT
# # Paranthesis , exponents , Multiplication , Division , Addition , Subtraction , left to right
# # # ()
# # **
# # * /
# # + -

# print(3 * 3 + 3 / 3 - 3)

# # BMI Calculator Challenge

# height = float(input("enter your height in m: "))
# weight = float(input("enter your weight in kg: "))

# # print(type(height))
# # print(type(weight))

# BMI = int((weight) / (height * height))
# print(BMI)

# Rounding a number 
print(8/3) # 2.6666666
print(int(8/3)) # to round the number use 'round' function.
print(round(8/3)) # 3
print(round(8/3,2)) # round to two decimal places. 2.67
print(round(2.6666,3)) # 2.667
print(8//3) #floor division use without converting into integer
print(type(8/3))
print(type(8//3))