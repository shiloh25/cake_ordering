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

        elif response == "menu":
            menu()

        else:
            print("Please enter yes or no")


def not_blank(question):

    while True:
        response = input(question)

        # if the response is blank, outputs error
        if response == "":
            print("Sorry this can't be blank. Please try again")
        else:
            return response


def cake_order(question):
    while True:

        cake_flavour = input(question).lower()

        if cake_flavour in cake_list:
            print("You have chosen {}".format(cake_flavour))
            cake_counter()
            topping_counter.counter = 1
            current_order["cake"] = cake_flavour
            break
        elif cake_flavour == "menu":
            menu()
            continue
        elif cake_flavour == "xxx":
            return cake_flavour
        else:
            print("Please choose an option from the menu")


def cake_counter():
    cake_counter.counter += 1
    return cake_counter.counter


def icing_order():
    while True:

        icing_flavour = input("\nWhat flavour icing would you like? ").lower()

        if icing_flavour in icing_list:
            print("You have chosen {} icing".format(icing_flavour))
            current_order["icing"] = icing_flavour
            break

        elif icing_flavour == "none":
            print("You have chosen no icing")
            current_order["icing"] = "none"
            break
        elif icing_flavour == "menu":
            menu()
            continue
        else:
            print("Please choose an option from the menu or none")


def which_toppings():
    current_order["toppings"] = []
    while topping_counter.counter <= 3:
        response = input("\nTopping {}: ".format(topping_counter.counter)).lower()
        if response in toppings_list:
            topping_counter()
            print("You have chosen {}".format(response))
            current_order["toppings"].append(response)
            continue

        elif response == "xxx":
            print("You have chosen no further toppings")
            break

        elif response == "menu":
            menu()

        else:
            print("Please choose an item from the menu or xxx for no more toppings")


def topping_counter():
    topping_counter.counter += 1
    return topping_counter.counter


def pickup_delivery(question):

    while True:
        response = input(question).lower()

        if response == "pickup" or response == "delivery":
            print("You have chosen {}".format(response))
            return response

        else:
            print("Please choose either pickup or delivery")


def get_address():
    while True:
        address = input("\nWhere would you like the order delivered? ").lower()
        number = any(map(str.isdigit, address))
        string = any(map(str.isalpha, address))
        if number == True and string == True:
            print("Your order will be delivered to {}".format(address))
            break
        else:
            print("Please enter a valid address")


def calculate_total(order_list):
    cake_cost = sum([cake_price[cake_list.index(order["cake"])] for order in order_list])
    icing_cost = sum([icing_price[icing_list.index(order["icing"])]
                      for order in order_list if order["icing"] != "none"])
    toppings_cost = sum([topping_price[toppings_list.index(topping)]
                         for order in order_list for topping in order["toppings"]])
    return cake_cost + icing_cost + toppings_cost


# main routine goes here
cake_list = ["chocolate", "strawberry", "vanilla", "lemon", "banana",
             "carrot", "pistachio", "coffee", "raspberry", "coconut", "funfetti"]
cake_price = [8, 8, 8, 8, 8, 8, 10, 10, 10, 10, 6]

icing_list = ["chocolate", "strawberry", "vanilla", "lemon", "coffee",
              "raspberry", "coconut", "caramel", "blueberry", "orange"]
icing_price = [2, 2, 2, 2, 3, 3, 3, 3, 3, 3]

toppings_list = ["chocolates", "strawberries", "raspberries", "coconut",
                 "blueberries", "oranges", "lemons", "sprinkles", "lollies", "caramel"]
topping_price = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2]

cake_counter.counter = 0
topping_counter.counter = 1

order_list = []
current_order = {}

while True:
    want_instructions = yes_no("Do you want to read the menu? ")

    if want_instructions == "yes" or want_instructions == "y":
        menu()
        break

    elif want_instructions == "no" or want_instructions == "n":
        break

while cake_counter.counter < 3:
    current_order = {}
    which_flavour = cake_order("\nWhat flavour cake would you like? ")
    if which_flavour == "xxx":
        break
    icing_order()

    want_toppings = yes_no("\nWould you like any toppings? ")

    if want_toppings == "yes" or want_toppings == "y":
        which_toppings()
    else:
        current_order["toppings"] = []

    order_list.append(current_order)

while True:
    name = not_blank("\nPlease enter a name for the order: ")

    order_option = pickup_delivery("\nWould you like pickup or delivery? ")
    if order_option == "pickup":
        break
    elif order_option == "delivery":
        get_address()
        break

total_price = calculate_total(order_list)
if order_option == "delivery":
    total_price += 5

print("\nOrder Summary:")
for idx, order in enumerate(order_list, start=1):
    print(f"Order {idx}:")
    print(f"  Cake: {order['cake'].capitalize()}")
    print(f"  Icing: {order['icing'].capitalize()}")
    if order['toppings']:
        print(f"  Toppings: {', '.join(topping.capitalize() for topping in order['toppings'])}")
        print()
    else:
        print("  Toppings: None")
        print()
if order_option == "delivery":
    print("Delivery Fee: $5")
print()

print("Total Price: ${}".format(total_price))
