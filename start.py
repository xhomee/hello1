import random
import pi_module

number = random.randint(1,100)
#print(f"number is {number}")

print(pi_module.pambu_doh)
print("Welcome to the Number Guessing Game!")
input_level = input("Choose a difficulty. Type 'easy' or 'hard': ")

def check_level(input_level):
    global life
    if input_level == "hard" or input_level == "h":
        print("You have 5 attempts remaining to guess the number.")
        life = 5
    elif input_level == "easy" or input_level == "e":
        print("You have 10 attempts remaining to guess the number.")
        life = 10
    return life

check_level(input_level)

def check_number(user_answer):
    global life
    global game
    if user_answer > 100 or user_answer < 0:
        print("incorrect answer")
        life = life -1
    elif user_answer == number:
        print(f"You got it! The answer was {number}.")
        #life = 0
        game = False
    elif user_answer > number:
        print("Too high.")
        life = life - 1
        print(f"You have {life} attempts remaining to guess the number.")
    elif user_answer < number:
        print("Too low.")
        life = life - 1
        print(f"You have {life} attempts remaining to guess the number.")
    return life



game = True

while game:
    if life == 0 and user_answer != number:
        print(f"You've run out of guesses, you lose. The answer was {number}.")
        game = False
    else:
        user_answer = int(input("Make a guess: "))
        check_number(user_answer)










#
# #check_level(input_level=input_level)
#
# # life = check_level(input_level=input_level)
# # print(life)
#
# def check_answer():
#     answer = int(input("введіть число "))
#     if answer > number:
#         print(life)
#         new_life = life - 1
#         print(new_life)
#
#     while new_life > 0:
#
#         print("gg")
#         break
#
#     print(f"sdfgsdfg2 {new_life}")
#
# check_answer()
# check_answer()
# check_answer()
# check_answer()
# check_answer()
# #print(f"sdfgsdfg3 {new_life}")
# #new_life = check_answer()
# #print(f"sdfsdfg {new_life}")
# #
# # while new_life > 0:
# #     new_life = check_answer()
# #     check_answer()
#
#
#
#





































# answer_level = input("Choose a difficulty. Type 'easy' or 'hard': ")
# if answer_level == "hard" or answer_level == "h":
#     lifes = 5
#     print("You have 5 attempts remaining to guess the number.")
#     #print("gg")
# elif answer_level == "easy" or answer_level == "e":
#     lifes = 10
#     print("You have 10 attempts remaining to guess the number.")
#
#
#
# def check_number(user_answer,lifes):
#
#     if user_answer > 100 or user_answer < 0:
#         print("incorrect answer")
#         lifes = lifes -1
#         print(f"we there {lifes}")
#     elif user_answer == number:
#         print("you win")
#         lifes = 0
#         pass
#     elif user_answer > number:
#         print("Ваше число більше ніж загадане")
#         lifes = lifes - 1
#         print(f"У вас залишилось {lifes} життів")
#     elif user_answer < number:
#         print("Ваше число меньше ніж загадане")
#         lifes = lifes - 1
#         print(f"У вас залишилось {lifes} життів")
#     return lifes
# print(lifes)
#
#
# #print(f"dfgsdfgsdfg {lifes}")
#
# while lifes > 0:
#     #print(new_lifes)
#     print(lifes)
#     user_answer = int(input("Make a guess: "))
#     check_number(user_answer,lifes)
#     pass
#
#
#

