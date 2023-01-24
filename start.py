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
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

first_step = input("You're at a cross road. Where do you want to go? Type ""left" ' or ' "right\n""")


if first_step == "Left" or first_step == "left" or first_step == "L" or first_step == "l":
    second_step = input("""You've come to a lake. There is an island in the middle of the lake. 
Type "wait" to wait for a boat. Type "swim" to swim across.\n""")
    if second_step == "Wait" or second_step == "wait" or second_step == "W" or second_step == "w":
        third_step = input("You arrive at the island unharmed. There is a house with 3 doors. "
                           "\nOne red, one yellow and one blue. Which colour do you choose?\n")
        if third_step == "Red" or third_step == "red" or third_step == "R" or third_step == "r":
            print("It's a room full of fire. Game Over.")
        elif third_step == "Blue" or third_step == "blue" or third_step == "B" or third_step == "b":
            print("You enter a room of beasts. Game Over.")
        elif third_step == "Yellow" or third_step == "yellow" or third_step == "Y" or third_step == "y":
            print("You found the treasure! You Win!")
        elif third_step == "xhomee":
            print("gg wp")
        else:
            print("You chose a door that doesn't exist. Game Over.")

    else:
        print("You get attacked by an angry trout. Game Over.")

else:
    print("You fell into a hole. Game Over.")
