import random

from art import logo

print(logo)
answer = random.randint(1, 100)


def show_answer():
    hint = input("Would you like to know the answer. Type 'y' for yes and 'n' for no: ")
    if hint == 'y':
        print(f"Pssst, the correct answer is {answer}")


def difficulty(level):
    if level == 'e':
        num = 10

    elif level == 'h':
        num = 5

    else:
        return "Invalid response"
    for i in range(num, 0, -1):
        print(f"You have {i} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))
        if guess == answer:
            return f"You got it! The answer was {answer}"
        elif guess < answer:
            print("Too low.")
            return
        elif guess > answer:
            print("Too high.")
            return
        if i == 1:
            return "You've run out of guesses, you lose."
        return
    return


print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
show_answer()
choose_difficulty = input("Choose a difficulty. Type 'e' for easy or 'h' for hard: ")
print(difficulty(choose_difficulty))
