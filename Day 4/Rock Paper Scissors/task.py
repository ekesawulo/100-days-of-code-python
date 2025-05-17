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

print('Welcome to rock-paper-scissors')
userInput = input('Type "rock", "paper" and "scissors"\n')

RPS = [rock, paper, scissors]
aiChoice = random.choice(RPS)
if userInput == 'rock' and aiChoice == paper:
    print('You lose! :(')
elif userInput == 'rock' and aiChoice == scissors:
    print('You win! :)')
elif userInput == 'paper' and aiChoice == rock:
    print('You win! :)')
elif userInput == 'paper' and aiChoice == scissors:
    print('You lose! :(')
elif userInput == 'scissors' and aiChoice == rock:
    print('You lose! :(')
elif userInput == 'scissoes' and aiChoice == paper:
    print('You win! :)')
elif userInput == aiChoice:
    print('Draw!')
else:
    print('You have entered an invalid response.')
