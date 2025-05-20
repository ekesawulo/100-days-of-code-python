import random

from art import logo

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def game_end(player_cards, dealer_cards):
    print(f"Your final hand: {player_cards}, final score: {sum(player_cards)}")
    print(f"Computer's final hand: {dealer_cards}, final score: {sum(dealer_cards)}")


def no_blackjack(player, dealer):
    no_winner = True
    while no_winner:
        hit_stand = input("Type 'y' to get another card, type 'n' to pass: ")
        if hit_stand == 'y':
            player.append(random.choice(cards))
            print(f"Your cards: {player}, current score: {sum(player)}")
            print(f"Computer's first card: {dealer[0]}")
            if sum(player) > 21 and 11 in player:
                for i in range(len(player)):
                    if player[i] == 11:
                        player[i] = 1
            elif sum(player) > 21:
                game_end(player, dealer)
                print("Bust! You lose")
                no_winner = False
        elif hit_stand == 'n':
            while sum(dealer) <= 16:
                dealer.append(random.choice(cards))
                if sum(dealer) > 21 and 11 in dealer:
                    for i in range(len(dealer)):
                        if dealer[i] == 11:
                            dealer[i] = 1
                if sum(dealer) > 21:
                    game_end(player, dealer)
                    print("Dealer went over! You win!")
                    no_winner = False
            if no_winner:
                if sum(dealer) > sum(player):
                    game_end(player, dealer)
                    print('You lose')
                    no_winner = False
                elif sum(dealer) < sum(player):
                    game_end(player, dealer)
                    print('You win!')
                    no_winner = False
                else:
                    game_end(player, dealer)
                    print('Draw!')
                    no_winner = False
        else:
            print('You have entered an invalid input, try again')


def blackjack():
    print(logo)
    player_hand = (random.choices(cards, k=2))
    dealer_hand = (random.choices(cards, k=2))
    print(f"Your cards: {player_hand}, current score: {sum(player_hand)}")
    print(f"Computer's first card: {dealer_hand[0]}")
    if sum(dealer_hand) == 21:
        game_end(player_hand, dealer_hand)
        print("Lose, opponent has Blackjack 😱")
    elif sum(player_hand) == 21:
        game_end(player_cards=player_hand, dealer_cards=dealer_hand)
        print("Win with a Blackjack 😎")
    else:
        no_blackjack(player_hand, dealer_hand)


ongoing_game = True
while ongoing_game:
    start = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
    if start == 'y':
        print("\n" * 20)
        blackjack()
    elif start == "n":
        ongoing_game = False
    else:
        print('You have entered an invalid input, try again')
