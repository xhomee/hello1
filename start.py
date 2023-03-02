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


def add_cards_to_hand(chose_role):
    if chose_role == "player":
        player_hand.append(random.choice(deck_cards))
    else:
        dealer_hand.append(random.choice(deck_cards))


def print_cards(chose_role):
    if chose_role == "your_cards":
        print(f"Your cards: {player_hand}, current score: {sum(player_hand)}")
    else:
        print(f"Computer's cards: {dealer_hand}, current score: {sum(dealer_hand)}\n")


game_started = True
turn = "player"
if start_game_one == "y":

    game_started = True
    first_hand()
    player_hand, dealer_hand = first_hand()
    print(f"Your cards: {player_hand}, current score: {sum(player_hand)}")
    print(f"Computer's first card: {dealer_hand[0]}\n")

else:
    print("gg, invalid value")
    game_started = False


def sum_cards_in_hand(cards_in_hand):
    if 11 in cards_in_hand and sum(cards_in_hand) > 21:
        cards_in_hand.remove(11)
        cards_in_hand.append(1)

    return cards_in_hand


def check_lose(player):
    global game_started
    global turn
    sum_player = sum(sum_cards_in_hand(player))

    if sum_player > 21:
        print("You lose this game\n")
        game_started = False


def check_win(player, dealer):
    global game_started
    sum_player = sum(sum_cards_in_hand(player))
    sum_dealer = sum(sum_cards_in_hand(dealer))

    if sum_player > sum_dealer or sum_dealer > 21:
        print("you win")
        game_started = False
    elif sum_player < sum_dealer or sum_dealer == 21:
        print("you lose")
        game_started = False
    elif sum_player == sum_dealer:
        print("draw")
        game_started = False
    else:
        print("404 error")


while game_started:
    global new_card

    if turn == "player":
        y = sum(sum_cards_in_hand(player_hand))
        if y == 21:
            turn = "g"
            continue
        else:
            new_card = input("Type 'y' to get another card, type 'n' to pass: \n")

            if new_card == "y":
                add_cards_to_hand(chose_role="player")
                sum_cards_in_hand(player_hand)
                sum_cards_in_hand(dealer_hand)
                print_cards(chose_role="your_cards")
                x = sum_cards_in_hand(player_hand)
                check_lose(player=x)

    elif turn != "player":
        print_cards(chose_role="dealer_cards")
        while sum(dealer_hand) < 17:
            add_cards_to_hand(chose_role="dealer")
            print_cards(chose_role="dealer_cards")
        x = sum_cards_in_hand(player_hand)
        y = sum_cards_in_hand(dealer_hand)
        check_win(player=x, dealer=y)

    else:
        print("invalid value")
        game_started = False
