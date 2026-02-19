# Randomisation and python list.

#Randomisation - Unpredictability in game like Tetris.
# random.randint(a,b) function both a,b are inclusive.
# random is a module develop by python team to make it easier for us to generate random number using randint(a,b) function.
#How to make our own module 
import random  
import my_module # module created by me.
random_integer = random.randint(1,10)
print(random_integer)

print(my_module.pi) # module created by me.

random_float = random.random() # Generate a random float number from 0 to 1 [exclusive]
print(random_float)

# uniform is used to generate random decimal or floating number. 
random_float = random.random() * 5 
print(random_float)


# How to create a random decimal number between 0 and 5.
# use randrange(start,stops,steps)
random_decimal = random.uniform(0,5) # uniform is used to generate random decimal or floating number. 
print(random_decimal)

#challenge of Day4

print("Welcome to coin toss program")
if random.randint(0,1) == 1:
    print("Heads")
elif random.randint(0,1) == 0:
    print("Tails")

#List {Data Structure}

fruits = ["cherry","mango","apple"] 
states_of_america = ["Alabama", "Alaska", "Arizona", "Arkansas", "California", "Colorado", 
             "Connecticut", "Delaware", "Florida", "Georgia", "Hawaii", "Idaho", 
             "Illinois", "Indiana", "Iowa", "Kansas", "Kentucky", "Louisiana", 
             "Maine", "Maryland", "Massachusetts", "Michigan", "Minnesota", 
             "Mississippi", "Missouri", "Montana", "Nebraska", "Nevada", 
             "New Hampshire", "New Jersey", "New Mexico", "New York", 
             "North Carolina", "North Dakota", "Ohio", "Oklahoma", "Oregon", 
             "Pennsylvania", "Rhode Island", "South Carolina", "South Dakota", 
             "Tennessee", "Texas", "Utah", "Vermont", "Virginia", "Washington", 
             "West Virginia", "Wisconsin", "Wyoming"]

print(states_of_america[-3]) # accessing each element of list.
states_of_america[0] = "alibaba" # change Albama to alibaba.
states_of_america.append("Canada") # add items to end of the list .
states_of_america.reverse() # reverses the list.
#states_of_america.clear() #clear the entire list.
states_of_america.sort() # sort the list.
states_of_america.pop(1) # Remove element at specific position.
states_of_america.insert(0,"Albama") # Insert element at specific position.
states_of_america.copy() #return a shallow copy of list.
states_of_america.extend(["Mexico","Cuba"]) # Add bunch of items in list.
print(states_of_america)

# Challenge Russian Rouellete
names_string = input("Give me everybody's names,seperated by a comma.\n")
names = names_string.split(", ")
print(len(names))
Name=random.choice(names) #Here we use random.choice to pick a random name from the list.
print(f"{Name} is going to buy the meal today!")