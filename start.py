import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
user_choose = input("Welcome to the game. Choose rock - 0 paper - 1 scissors -2 ")
#user_choose = "1"
# rock_var = 0
# paper_var = 1
# scissors_var = 2
typess = [rock,paper,scissors]
#variable_computer = random.randint(0,2) # 0,1,2

x = random.choice(typess)
#print(x)

#typess = [rock_var,paper_var,scissors_var]
#print(typess)


if user_choose == "0":
    print(typess[0])
    print("Computer choose")
    if x == typess[2]:
        print(x)
        print("u win")
    elif x == typess[0]:
        print(x)
        print("draw")
    elif x == typess[1]:
        print(x)
        print("u lose")
elif user_choose == "1":
    print(typess[1])
    print("Computer choose")
    if x == typess[2]:
        print(x)
        print("u lose")
    elif x == typess[0]:
        print(x)
        print("u win")
    elif x == typess[1]:
        print(x)
        print("draw")
elif user_choose == "2":
    print(typess[2])
    print("Computer choose")
    if x == typess[2]:
        print(x)
        print("draw")
    elif x == typess[0]:
        print(x)
        print("u lose")
    elif x == typess[1]:
        print(x)
        print("u win")
else:
    print("Unknown choose")


# Rock wins against scissors.
# Scissors win against paper.
# Paper wins against rock.

# if user_choose == "0":
#     print(rock)
#     if variable_computer == 2:
#         print("u win")
#         print(variable_computer)
#     elif variable_computer == 0:
#         print("draw")
#         print(variable_computer)
#     else:
#         print("u lose")
#         print(variable_computer)
# elif user_choose == "1":
#     print(paper)
# elif user_choose == "2":
#     print(scissors)
# else:
#     print("Unknown choose")
#
