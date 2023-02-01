import random
import pi_module

word_list = ["ardvark", "baboon", "camel"]
#pi_module.world_list
chosen_word = random.choice(word_list)
lives = 6
end_of_game = False

print(pi_module.logo)

# NEED add _ in list
add_underscore = []
for letters in chosen_word:
    add_underscore.append("_")


while not end_of_game:
    while not lives <= 0:
        guess = input("Enter a letter ").lower()  # original
        if guess in add_underscore:
            print("This letter already exists")
            print("")

        elif guess in chosen_word:
            for position in range(len(chosen_word)):
                letter = chosen_word[position]
                if letter == guess:
                    add_underscore[position] = letter
            break

        else:
            lives -=1
            print(f"{guess} not in the word")
            break


    print(pi_module.stages[lives])
    print(f"{' '.join(add_underscore)}    word length: {len(chosen_word)}")
    print("")

    if lives <= 0:
        end_of_game = True
        print("Your lose")

    if '_' not in add_underscore:
        end_of_game = True
        print("You win")




