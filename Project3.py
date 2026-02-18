print(''''
            .-.
           [.-''-.,
           |  //`~\)
           (<| 0\0|>_
           ";\  _"/ \\_ _,
          __\|'._/_  \ '='-,
         /\ \    || )_///_\>>
        (  '._ T |\ | _/),-'
         '.   '._.-' /'/ |
         | '._   _.'`-.._/
   snd   ,\ / '-' |/
         [_/\-----j
    _.--.__[_.--'_\__
   /         `--'    '---._
  /  '---.  -'. .'  _.--   '.
  \_      '--.___ _;.-o     /
    '.__ ___/______.__8----'
''')
print('''

*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************''')

print("Welcome to the treasure Island")
print("Your mission is to find the treasure.")
user_input = input("left or right? ")
if (user_input == "right") or( user_input == "Right"):
    print("oops! you fall into a hole.Better luck next time.GAME OVER!! ")
elif (user_input == "left") or (user_input == "Left"):
    print("Wooho their is a big river to cross.")
    step2 = input("Do you want to swim or wait for the boat ?")
    if (step2 == "swim") or (step2 == "Swim"):
        print("oh no you have been attacked by trout.GAME OVER!! ") 
    elif (step2 == "wait") or (step2 == "Wait"):
        print("Their a 3 Magical door Red, Blue, Yellow choose one to reach your destiny ")
        step3 = input("Be careful.Which door do you want to choose? ")
        if (step3 =="Red") or (step3 == "red"):
            print("You are dead! Burned by fire.Game Over!! ")
        elif (step3 == "Blue") or (step3 == "blue"):
            print("You are dead! Eaten by beasts.Game Over!! ")
        elif (step3 == "Yellow") or (step3 == "yellow"):
            print("You Win,Congratulations. ")
        else:
            print("Game Over!!")