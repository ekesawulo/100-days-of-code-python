# placeholder in letter template
PLACEHOLDER = "[name]"
with open("Day 24/Input/Names/invited_names.txt") as file:
    names = file.readlines()

with open("Day 24/Input/Letters/starting_letter.txt") as file:
    letter_template = file.read()
for name in names:
    name = name.strip()
    with open(file=f"Day 24/Output/ReadyToSend/{name}.txt", mode="w") as file:
        personalised_letter = letter_template.replace(PLACEHOLDER, f"{name}")
        file.write(personalised_letter)
