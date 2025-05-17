MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def sufficient_resources(selection):
    for i, j in MENU[selection]["ingredients"].items():
        # checks if resources are enough before prepare coffee function
        if resources[i] < j:
            print(f"Sorry there is not enough {i}.")
            return False
    return True


def process_coins():
    print("Please insert coins.")
    # apparently I can improve this by looping through a dictionary
    # def process_coins():
    #     print("Please insert coins.")
    #     coin_values = {
    #         "quarters": 0.25,
    #         "dimes": 0.10,
    #         "nickels": 0.05,
    #         "pennies": 0.01
    #     }
    #     total = 0
    #     for coin, value in coin_values.items():
    #         count = int(input(f"How many {coin}?: "))
    #         total += count * value
    #     return total
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickels = int(input("How many nickels?: "))
    pennies = int(input("How many pennies?: "))
    return quarters * .25 + dimes * .1 + nickels * .05 + pennies * .01


def make_coffee(inventory, selection):
    total = process_coins()
    coffee_cost = MENU[selection]["cost"]
    if total >= coffee_cost:
        if total > coffee_cost:
            print(f"Here is ${total - coffee_cost:.2f} in change")
        print(f"Here is your {selection} ☕️. Enjoy!")
        inventory["money"] += coffee_cost
        for i, j in MENU[selection]["ingredients"].items():
            inventory[i] -= j
    else:
        print("Sorry that's not enough money. Money refunded.")


def display_report(inventory):
    for i, j in inventory.items():
        if i in ("water", "milk"):
            j = f"{j}ml"
        elif i == "coffee":
            j = f"{j}g"
        elif i == "money":
            j = f"${j:.2f}"
        else:
            j = str(j)
        print(f"{i.capitalize()}: {j}")


def get_order():
    while True:
        # input validation
        user_input = input("What would you like? (espresso/latte/cappuccino): ").lower()
        if user_input in {"espresso", "latte", "cappuccino",
                          "off", "report"}:
            # learning to use idiomatic python
            return user_input
        else:
            print("Invalid input, please enter one of the given options.")


resources['money'] = 0
is_on = True
while is_on:
    order = get_order()
    if order == "off":
        is_on = False
    elif order == "report":
        display_report(resources)
    else:
        if sufficient_resources(order):
            make_coffee(resources, order)
