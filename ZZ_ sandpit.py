import pandas as pd
from tabulate import tabulate

# Functions go here
def menu():
    cake = pd.DataFrame(list(zip(cake_list, cake_price)),
                        columns=['Cakes', 'Price'])
    print(tabulate(cake, showindex=False, headers=cake.columns))
    print()
    icing = pd.DataFrame(list(zip(icing_list, icing_price)),
                        columns=['Icing', 'Price'])
    print(tabulate(icing, showindex=False, headers=icing.columns))
    print()
    topping = pd.DataFrame(list(zip(toppings_list, topping_price)),
                        columns=['Toppings', 'Price'])
    print(tabulate(topping, showindex=False, headers=topping.columns))


def yes_no(question):
    while True:
        response = input(question).lower()
        if response in ["yes", "y"]:
            return "yes"
        elif response in ["no", "n"]:
            return "no"
        else:
            print("Please enter yes or no")


def cake_order():
    while True:
        cake_flavour = input("\nWhat flavour cake would you like? ").lower()
        if cake_flavour in cake_list:
            print("You have chosen {}".format(cake_flavour))
            cake_counter()
            topping_counter.counter = 1  # Reset topping counter here
            break
        elif cake_flavour == "menu":
            menu()
            continue
        else:
            print("Please choose an option from the menu\n")


def cake_counter():
    cake_counter.counter += 1
    return cake_counter.counter


def icing_order():
    while True:
        icing_flavour = input("\nWhat flavour icing would you like? ").lower()
        if icing_flavour in icing_list:
            print("You have chosen {} icing".format(icing_flavour))
            break
        elif icing_flavour == "none":
            print("You have chosen no icing")
            break
        elif icing_flavour == "menu":
            menu()
            continue
        else:
            print("Please choose an option from the menu or none\n")


def which_toppings():
    while topping_counter.counter <= 3:
        response = input("Topping {}: ".format(topping_counter.counter)).lower()
        if response in toppings_list:
            topping_counter()
            continue
        elif response == "xxx":
            break
        elif response == "menu":
            menu()
        else:
            print("Please choose an item from the menu or xxx for no more toppings\n")


def topping_counter():
    topping_counter.counter += 1
    return topping_counter.counter


# Main routine goes here
cake_list = ["chocolate", "strawberry", "vanilla", "lemon", "banana",
             "carrot", "pistachio", "coffee", "raspberry", "coconut", "funfetti"]
cake_price = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

icing_list = ["chocolate", "strawberry", "vanilla", "lemon", "coffee",
              "raspberry", "coconut", "caramel", "blueberry", "orange"]
icing_price = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

toppings_list = ["chocolates", "strawberries", "raspberries", "coconut",
                 "blueberries", "oranges", "lemons", "sprinkles", "lollies", "caramel"]
topping_price = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

cake_counter.counter = 0
topping_counter.counter = 1

while True:
    want_instructions = yes_no("Do you want to read the menu? ")
    if want_instructions in ["yes", "y"]:
        menu()
        break
    elif want_instructions in ["no", "n"]:
        break

while cake_counter.counter <= 3:
    cake_order()
    icing_order()
    while True:
        want_toppings = yes_no("Would you like any toppings? ")
        if want_toppings in ["yes", "y"]:
            which_toppings()
            break
        elif want_toppings in ["no", "n"]:
            print("You have chosen no toppings")
            break