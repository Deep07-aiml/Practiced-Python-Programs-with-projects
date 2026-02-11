print('Hello world\nHello world\nHello world!')
print("Hello" + "Deep") #NO space between them
print("Hello"+ " " + "Deep") # Adding space between them
print("Hello" + " Deep") # Added space in Name

#Debugging 1.2
#Fix the below code 
print("Day 1 - String Manipulation")
print("String Concatenation is done with the '+' " "sign.") #You can add + sign for space in between
print('e.g. print("Hello " + "world")')
print("New lines can be created with a backlash and n.")

#input() function
print("Hello " + input("What is your name?")) #Thony python to know how it is executing the code.

#Day 1.3 Exercise
name = input('Enter your name:') 
print(name)                 # len() function count the length of a string
text = print(len(name))
print( len( input('What is your name ') ) ) 

#Day1.4 Variables Exercise
a = int(input("a:"))  #error :-  unsupported operand type(s) for -: 'str' and 'str' 
b = int(input("b:"))  #Occur because In python3 input () function returns a string 
a = a + b
b = a - b  #swap two number without third variable
a = a - b
print(a)
print(b)

a = int(input("a:"))  #error :-  unsupported operand type(s) for -: 'str' and 'str' 
b = int(input("b:"))  #Occur because In python3 input () function returns a string 
c = a
a = b
b = c
print(a)
print(b)


time_until_midnight = "5"
print("There are "+time_until_midnight+" hours until midnight")

input = "5"
print("There are " + input + " hours until midnight")

#time_until_midnight = "5"
#print("There are " + time_until_Midnight + " hours until midnight")  #NameError time_until_Midnight


#Types of error I learned 
#1 SyntaxError ("hello world ) No closing quote
#2 NameError ("hllo wrld") invalid name used
#3 EOR parsing Error ( close bracket is missing