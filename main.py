import importlib
import time

stock = "stock.py"
portfolio = "portfolio.py"

importlib.import_module(stock)
importlib.import_module(portfolio)

# Dict to create the main menu
main_menu = dict()
main_menu["A"] = "View Portfolio"
main_menu["B"] = "View Transfer History"
main_menu["C"] = "View Transaction History"
main_menu["D"] = "Make Transfer"
main_menu["E"] = "Search Stock"

# Saves portfolio instance in memory
main_portfolio = portfolio.__init__()


def print_menu():
    print("\n\n--------------------------------")
    print("       Stock Machine Menu      ")
    print("--------------------------------")
    for key, value in main_menu:
        print("{0}.  {1}").format(key, value)

    eval_input()


def eval_input():
    user_input = input("Enter your choice: ")

    if (user_input.upper() == "A"):
        main_portfolio.view_portfolio()
        print("\n\n--------------------------------")
        print(r"\n\--------------------------------")
    elif (user_input == "B"):
        main_portfolio.view_transfer_history()
        print("\n\n--------------------------------")
        print(r"\n\--------------------------------")
    elif (user_input == "C"):
        main_portfolio.view_transaction_history()
        print("\n\n--------------------------------")
        print(r"\n\--------------------------------")
    elif (user_input == "D"):
        transfer_type = input(
            "Enter deposit type: A. Deposit   B. Withdrawal ")
        transfer_amount = input("Enter transfer amount: $")

        if (transfer_type == "A"):
            main_portfolio.make_transfer(True, transfer_amount)
        else:
            main_portfolio.make_transfer(False, transfer_amount)

        print("\n\n--------------------------------")
        print(r"\n\--------------------------------")
    elif (user_input == "E"):
        print("\n\n--------------------------------")
        print(r"\n\--------------------------------")
    else:
        print("There was an issue with your input try again.")
        time.sleep(2)
        print_menu()
        print("\n\n--------------------------------")
        print(r"\n\--------------------------------")


def main():
    print("Welcome to the Stock Machine Command Line App.")
    print("Created by Trevor Njeru.")

    name = input("What is your name? ")
    dobYear = input("What year were you born? ")
    main_portfolio.__init__(name, dobYear)

    print_menu()
