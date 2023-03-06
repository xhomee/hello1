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
        life = life - 1
    elif user_answer == number:
        print(f"You got it! The answer was {number}.")
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

