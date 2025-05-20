from art import logo


def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


operators = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}


def calculator():
    print(logo)
    first_num = float(input("Enter the first number: "))
    total = 0
    isSolving = True
    while isSolving:
        for operator in operators:
            print(f"{operator}")
        chosen_operator = input("Choose a mathematical operator from above: ")
        second_num = float(input("Enter the second number: "))
        for operator in operators:
            if chosen_operator == operator:
                total = operators[chosen_operator](first_num, second_num)
        print(f"{first_num} {chosen_operator} {second_num} = {total}")
        keep_solving = input(
            f"Type 'y' to continue calculating with {total}, or type 'n' to start a new calculation: \n")
        if keep_solving == "y":
            first_num = total
        else:
            print("\n" * 20)
            calculator()


calculator()
