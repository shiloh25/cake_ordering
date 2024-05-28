# functions go here
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

        else:
            print("Please choose an item from the menu or xxx for no more toppings\n")


# main routine goes here
cake_list = ["chocolate", "strawberry", "vanilla", "lemon", "banana",
             "carrot", "pistachio", "coffee", "raspberry", "coconut", "funfetti"]
icing_list = ["chocolate", "strawberry", "vanilla", "lemon", "coffee",
             "raspberry", "coconut", "caramel", "blueberry", "orange"]
toppings_list = ["chocolates", "strawberries", "raspberries", "coconut",
                 "blueberries", "oranges", "lemons", "sprinkles", "lollies", "caramel"]

while True:
    want_instructions = yes_no("Do you want to read the menu? ")

    if want_instructions == "yes" or want_instructions == "y":
        print("menu go here\n")
        break

    elif want_instructions == "no" or want_instructions == "n":
        break

while True:

    cake_flavour = input("What flavour cake would you like? ").lower()

    if cake_flavour in cake_list:
        print("You have chosen {}".format(cake_flavour))
        break

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

    else:
        print("Please choose an option from the menu or none\n")

while True:
    want_toppings = yes_no("Would you like any toppings? ")

    if want_toppings == "yes" or want_toppings == "y":
        break

    if want_toppings == "no" or want_toppings == "n":
        print("You have chosen no toppings")
        break

while want_toppings == "yes" or want_toppings == "y":
    topping1 = which_toppings("What is the first topping you would like? ")
    if topping1 is None:
        break

    topping2 = which_toppings("What is the second topping you would like? ")
    if topping2 is None:
        break

    topping3 = which_toppings("What is the third topping you would like? ")
    if topping3 is None:
        break
