# # Randomisation and python list.

# #Randomisation - Unpredictability in game like Tetris.
# # random.randint(a,b) function both a,b are inclusive.
# # random is a module develop by python team to make it easier for us to generate random number using randint(a,b) function.
# #How to make our own module 
import random  
# import my_module # module created by me.
# random_integer = random.randint(1,10)
# print(random_integer)

# print(my_module.pi) # module created by me.

# # Generate a random floating number from 0 to 1[exclusive]
# random_float = random.random()
# print(random_float)
 
# random_float = random.random() * 5 
# print(random_float)


# # How to create a random decimal number between 0 and 5.
# random_decimal = random.uniform(0,5) # uniform is used to generate random decimal or floating number. 
# print(random_decimal)

# #challenge of Day4

# print("Welcome to coin toss program")
# if random.randint(0,1) == 1:
#     print("Heads")
# elif random.randint(0,1) == 0:
#     print("Tails")

# #List[] is a {Data Structure}

# fruits = ["cherry","mango","apple"] 
# states_of_america = ["Alabama", "Alaska", "Arizona", "Arkansas", "California", "Colorado", 
#              "Connecticut", "Delaware", "Florida", "Georgia", "Hawaii", "Idaho", 
#              "Illinois", "Indiana", "Iowa", "Kansas", "Kentucky", "Louisiana", 
#              "Maine", "Maryland", "Massachusetts", "Michigan", "Minnesota", 
#              "Mississippi", "Missouri", "Montana", "Nebraska", "Nevada", 
#              "New Hampshire", "New Jersey", "New Mexico", "New York", 
#              "North Carolina", "North Dakota", "Ohio", "Oklahoma", "Oregon", 
#              "Pennsylvania", "Rhode Island", "South Carolina", "South Dakota", 
#              "Tennessee", "Texas", "Utah", "Vermont", "Virginia", "Washington", 
#              "West Virginia", "Wisconsin", "Wyoming"]

# print(states_of_america[-3]) # accessing each element of list by using indexing.
# states_of_america[0] = "alibaba" # change Albama to alibaba.
# states_of_america.append("Canada") # add items to end of the list .
# states_of_america.reverse() # reverses the list.
# #states_of_america.clear() #clear the entire list.
# states_of_america.sort() # sort the list.
# states_of_america.pop(1) # Remove element at specific position.
# states_of_america.insert(0,"Albama") # Insert element at specific position.
# states_of_america.copy() #return a shallow copy of list.
# states_of_america.extend(["Mexico","Cuba"]) # Add bunch of items in list.
# print(states_of_america)

# # Challenge Who's Paying
# names_string = input("Give me everybody's names,seperated by a comma.\n")
# names = names_string.split(", ")
# a = len(names)
# b = random.randint(0,a-1)
# c = names[b]
# print(f"{c} is going to buy the meal today")
# # random.choice picks a random names from the list.
# d = random.choice(names)
# print(f"{d} will pay today!")

# #Index out of range Error :- list starts from 0 not 1.

# # Nested list

# # dirty_dozen = ["Spinach", "Strawberries", "Kale", "Collard"," Mustard Greens",
# #                     "Grapes", "Peaches", "Cherries", "Nectarines", "Pears",
# #                     "Apples", "Blackberries", "Green Beans", "Blueberries"]

# fruits = ["Strawberries","Grapes","Cherries","Pears","Apples","Blackberries","Blueberries"]
# vegetables = ["Kale", "Collard"," Mustard Greens","Peaches","Nectarines","Green Beans"]

# dirty_dozen = [fruits,vegetables]
# print(dirty_dozen)

# Challenge Treasure
row1 = ["⬜","⬜","⬜"]
row2 = ["⬜","⬜","⬜"]
row3 = ["⬜","⬜","⬜"]
map = [row1,row2,row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure")
a = (map[0][0],map[0][1],map[0][2],
     map[1][0],map[1][1],map[1][2],
     map[2][0],map[2][1],map[2][2])
print(f"{a}")
