import random

friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]
random_Index = random.randint(0, 4)
print(f'{friends[random_Index]} should pay the bill.')
print(f'{random.choice(friends)} should pay the bill.')
