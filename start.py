import random
import pi_module

print(pi_module.logo)
start_game_one = input("Do you want to play a game of Blackjack? Type 'y' or 'n': \n")


deck_cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def first_hand():
    player_hand = []
    dealer_hand = []
    player_hand.append(random.choice(deck_cards))
    player_hand.append(random.choice(deck_cards))

    dealer_hand.append(random.choice(deck_cards))
    dealer_hand.append(random.choice(deck_cards))
    return player_hand, dealer_hand


def add_cards_to_player_hand():
    player_hand.append(random.choice(deck_cards))
    return player_hand


def add_cards_to_dealer_hand():
    dealer_hand.append(random.choice(deck_cards))
    return dealer_hand


def print_your_cards():
    print(f"Your cards: {player_hand}, current score: {sum(player_hand)}")
    #print(f"Computer's cards: {dealer_hand}, current score: {sum(dealer_hand)}\n")


def print_dealer_cards():
    print(f"Computer's cards: {dealer_hand}, current score: {sum(dealer_hand)}\n")


if start_game_one == "y":
    game_started = True
    first_hand()
    player_hand, dealer_hand = first_hand()
    print(f"Your cards: {player_hand}, current score: {sum(player_hand)}")
    print(f"Computer's first card: {dealer_hand[0]}\n")
else:
    print("gg, invalid value")
    game_started = False


while game_started:
    new_card = input("Type 'y' to get another card, type 'n' to pass: \n")

    if new_card == "y":
        add_cards_to_player_hand()
        print_your_cards()
        if sum(player_hand) > 21:
            print("You lose this game\n")
            game_started = False
        elif sum(dealer_hand) < 17:
            add_cards_to_dealer_hand()
            if sum(dealer_hand) > 21:
                print("You win this game\n")
                game_started = False
    elif new_card == "n":
        print_dealer_cards()
        while sum(dealer_hand) < 17:
            add_cards_to_dealer_hand()
            print_dealer_cards()
        if sum(dealer_hand) > 21:
            print("You win this game\n")
            game_started = False
        elif sum(player_hand) > sum(dealer_hand):
            print("you win\n")
            game_started = False
        elif sum(player_hand) == sum(dealer_hand):
            print("draw\n")
            game_started = False
        elif sum(player_hand) < sum(dealer_hand):
            print("you lose\n")
            game_started = False
    else:
        print("invalid value")
        game_started = False
