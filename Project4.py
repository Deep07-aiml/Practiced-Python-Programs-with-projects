#Rock Paper Scissor game
import random
rock = ('''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)''')

paper = ('''
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)''')

scissor = ('''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)''')

game_images = [rock,paper,scissor]
user = int(input("What do you choose? Type 0 for Rock,1 for Paper or 2 for Scissors. \n"))
print(game_images[user])
print(f"you chose: {user}")
computer = random.randint(0,2)
print(game_images[computer])
print(f"computer chose {computer}")

if user == computer:
    print("Draw")
elif user == 0 and computer == 1:
    print("computer wins")
elif  user == 0 and computer == 2:
    print("user wins")
elif user == 1 and computer == 0:
    print("user wins")
elif user == 1 and computer == 2:
    print("computer wins")
elif user == 2 and computer == 0:
    print("computer wins")
elif user == 2 and computer == 1:
    print("user wins")
else:
    print("Invalid choice")