import pandas as pd
from tabulate import tabulate


# functions go here
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

        if response == "yes" or response == "y":
            return "yes"

        elif response == "no" or response == "n":
            return "no"

        else:
            print("please enter yes or no")


def which_toppings(question):

    while True:
        response = input(question).lower()

        if response in toppings_list:
            print("You have chosen {}\n".format(response))
            return response

        elif response == "xxx":
            print("You have chosen no further toppings\n")
            return None

        elif response == "menu":
            return "menu"
        
        else:
            print("Please choose an item from the menu or xxx for no more toppings\n")


# main routine goes here
cake_list = ["chocolate", "strawberry", "vanilla", "lemon", "banana",
             "carrot", "pistachio", "coffee", "raspberry", "coconut", "funfetti"]
cake_price = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

icing_list = ["chocolate", "strawberry", "vanilla", "lemon", "coffee",
              "raspberry", "coconut", "caramel", "blueberry", "orange"]
icing_price = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

toppings_list = ["chocolates", "strawberries", "raspberries", "coconut",
                 "blueberries", "oranges", "lemons", "sprinkles", "lollies", "caramel"]
topping_price = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

while True:
    want_instructions = yes_no("Do you want to read the menu? ")

    if want_instructions == "yes" or want_instructions == "y":
        menu()
        break

    elif want_instructions == "no" or want_instructions == "n":
        break

while True:

    cake_flavour = input("What flavour cake would you like? ").lower()

    if cake_flavour in cake_list:
        print("You have chosen {}".format(cake_flavour))
        break
    elif cake_flavour == "menu":
        menu()
        continue
    else:
        print("Please choose an option from the menu\n")

while True:

    icing_flavour = input("What flavour icing would you like? ").lower()

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

while True:
    want_toppings = yes_no("Would you like any toppings? ")

    if want_toppings == "yes" or want_toppings == "y":
        break

    elif want_toppings == "no" or want_toppings == "n":
        print("You have chosen no toppings")
        break

while want_toppings == "yes" or want_toppings == "y":
    topping1 = which_toppings("What is the first topping you would like? ")
    if topping1 is None:
        break
    elif topping1 == "menu":
        menu()

    topping2 = which_toppings("What is the second topping you would like? ")
    if topping2 is None:
        break
    elif topping2 == "menu":
        menu()

    topping3 = which_toppings("What is the third topping you would like? ")
    if topping3 is None:
        break
    elif topping3 == "menu":
        menu()
