from game_data import data
from pi_module import vs, higher_lower
import random

user_score = 0
game_on = True


def randoms():
    random_answer = random.choice(data)
    random_name = random_answer['name']
    random_count = random_answer['follower_count']
    random_description = random_answer['description']
    random_country = random_answer['country']
    return random_answer, random_name, random_count, random_description, random_country


random_answer, random_name, random_count, random_description, random_country = randoms()
random_answer2, random_name2, random_count2, random_description2, random_country2 = randoms()


def check_who_biggest():
    global user_score
    if random_count > random_count2:
        return random_count
    elif random_count2 > random_count:
        return random_count2
    else:
        user_score += 1
        return random_count2


print(higher_lower)
a_print =(f'Answer A: {random_name}, a {random_description}, from {random_country} \n'
          f'{vs}\nAnswer B: {random_name2}, a {random_description2}, from {random_country2} ')
print(a_print)


while game_on:
    answer = input("\nWho has more followers? Type 'A' or 'B': ")
    if answer == "a" or answer == "A":
        if random_count == check_who_biggest():
            user_score += 1
            print(f"\nYou score: {user_score}\n")
            random_answer2, random_name2, random_count2, random_description2, random_country2 = randoms()
            print(f'\nAnswer A: {random_name}, a {random_description}, from {random_country}')
            print(vs)
            print(f'Answer B: {random_name2}, a {random_description2}, from {random_country2}')
        else:
            input(f"You lose. you score {user_score}")
            game_on = False
    elif answer == "b" or answer == "B":
        if random_count2 == check_who_biggest():
            user_score += 1
            print(f"\nYou score: {user_score}\n")
            random_answer, random_name, random_count, random_description, random_country = randoms()
            print(f'\nAnswer A: {random_name}, a {random_description}, from {random_country}')
            print(vs)
            print(f'Answer B: {random_name2}, a {random_description2}, from {random_country2}')
        else:
            input(f"You lose. you score {user_score}")
            game_on = False
    elif answer == "xhome":
        user_score += 999
        print(f"\nYou score: {user_score}\n")
    else:
        input(f"You lose. you score {user_score}")
        game_on = False
