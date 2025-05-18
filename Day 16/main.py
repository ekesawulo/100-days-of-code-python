from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()


def get_order():
    while True:
        user_input = input(f"What would you like? {menu.get_items()} ")
        if user_input not in {"espresso", "latte", "cappuccino", "off", "report"}:
            print("Invalid input, please enter one of the given options.")
        return user_input


is_on = True
while is_on:
    choice = get_order()
    if choice == "off":
        is_on = False
    elif choice == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(choice)
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            coffee_maker.make_coffee(drink)
