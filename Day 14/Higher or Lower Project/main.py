import random

import art
import game_data


def output_description(bio):
    """Helps to avoid rewriting verbose bio statement"""
    return f"{bio['name']}, a {bio['description']}, from {bio['country']}"


def get_guess():
    while True:
        guess = input("Who has more followers? Type 'a' or 'b': ").lower()
        if guess != "a" and guess != "b":
            print("Invalid response, please type 'a' or 'b'")
        else:
            return guess


def get_random_option():
    return random.choice(game_data.data)


def check_guess(a, b, guess):
    return ((guess == "a" and a["follower_count"] > b["follower_count"]) or
            (guess == "b" and b["follower_count"] > a["follower_count"]))


def higher_lower():
    print(art.logo)
    winning = True
    wins = 0
    option_1 = get_random_option()
    while winning:
        option_2 = get_random_option()
        while option_2 == option_1:
            option_2 = get_random_option()
        print(f"Compare A: {output_description(option_1)} ")
        print(art.vs)
        print(f"Against B: {output_description(option_2)}")
        user_guess = get_guess()
        print("\n" * 20)
        print(art.logo)
        if check_guess(option_1, option_2, user_guess):
            wins += 1
            option_1 = option_2
            print(f"You're right! Current score {wins}")
        else:
            print(f"Sorry, that's wrong. Final score: {wins}")
            print(f"{output_description(option_1)} has "
                  f"{option_1['follower_count']} million followers and "
                  f"{output_description(option_2)} has {option_2['follower_count']} million followers.")
            winning = False


higher_lower()
