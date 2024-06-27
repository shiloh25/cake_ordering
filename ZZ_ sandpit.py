import pandas as pd
from tabulate import tabulate


# functions go here
# function that shows the menu
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


# checks that an input is either yes or no
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


# checks that an input is not blank
def not_blank(question):
    while True:
        response = input(question)

        # if the response is blank, outputs error
        if response == "":
            print("Sorry this can't be blank. Please try again")
        else:
            return response


# cake ordering function
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


# function to count the number of cakes
def cake_counter():
    cake_counter.counter += 1
    return cake_counter.counter


# icing ordering function
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


# topping ordering counter
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


# function to count number of toppings
def topping_counter():
    topping_counter.counter += 1
    return topping_counter.counter


# function to check users answer is either pickup or delivery
def pickup_delivery(question):
    while True:
        response = input(question).lower()

        if response == "pickup" or response == "delivery":
            print("You have chosen {}".format(response))
            return response

        else:
            print("Please choose either pickup or delivery")


# function to check that an input has both numbers and letters
def get_address():
    while True:
        address = input("\nWhere would you like the order delivered? ").lower()
        number = any(map(str.isdigit, address))
        string = any(map(str.isalpha, address))
        if number is True and string is True:
            print("Your order will be delivered to {}".format(address))
            return address
        else:
            print("Please enter a valid address")


# function to check that an input is only numbers
def num_check(question, error):
    valid = False
    while not valid:

        response = input(question)

        if response.isdigit():
            return response
        else:
            print(error)


# function to calculate order cost and return individual prices
def calculate_total(order_list):
    individual_prices = []
    cake_cost = sum([cake_price[cake_list.index(order["cake"])] for order in order_list])
    icing_cost = sum([icing_price[icing_list.index(order["icing"])]
                      for order in order_list if order["icing"] != "none"])
    toppings_cost = sum([topping_price[toppings_list.index(topping)]
                         for order in order_list for topping in order["toppings"]])

    for order in order_list:
        cake = cake_price[cake_list.index(order["cake"])]
        icing = icing_price[icing_list.index(order["icing"])] if order["icing"] != "none" else 0
        toppings = sum([topping_price[toppings_list.index(topping)] for topping in order["toppings"]])
        individual_prices.append({
            "cake": cake,
            "icing": icing,
            "toppings": toppings
        })

    total_cost = cake_cost + icing_cost + toppings_cost
    return total_cost, individual_prices


# function to check users input is either cash or credit
def cash_credit(question):
    while True:
        response = input(question).lower()

        if response == "cash" or response == "ca":
            return "cash"

        elif response == "credit" or response == "cr":
            return "credit"

        else:
            print("Please choose a valid payment method\n")


# Main routine goes here
# menu and price lists
cake_list = ["chocolate", "strawberry", "vanilla", "lemon", "banana",
             "carrot", "pistachio", "coffee", "raspberry", "coconut", "funfetti"]
cake_price = [8, 8, 8, 8, 8, 8, 10, 10, 10, 10, 6]

icing_list = ["chocolate", "strawberry", "vanilla", "lemon", "coffee",
              "raspberry", "coconut", "caramel", "blueberry", "orange"]
icing_price = [2, 2, 2, 2, 3, 3, 3, 3, 3, 3]

toppings_list = ["chocolates", "strawberries", "raspberries", "coconut",
                 "blueberries", "oranges", "lemons", "sprinkles", "lollies", "caramel"]
topping_price = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2]

# cake counter and topping counter
topping_counter.counter = 1

# order list and dictionary
order_list = []
current_order = {}
name_list = []

while True:
    cake_counter.counter = 0
    # first loop to ask user if they would like to read the menu
    print("\n***** Welcome to the Cake Ordering Program! *****")
    print("You can order up to 3 cakes per order with up to 3 toppings per cake")
    print("At any time, you can answer 'menu' to view the menu")
    while True:
        want_instructions = yes_no("\nDo you want to read the menu? ")

        if want_instructions == "yes" or want_instructions == "y":
            menu()
            break

        elif want_instructions == "no" or want_instructions == "n":
            break

    # loop to get the users order, breaks after three cakes as that is the -
    # - maximum order
    while cake_counter.counter < 3:
        current_order = {}
        # use cake ordering function to get cake
        which_flavour = cake_order("\nWhat flavour cake would you like? ")
        if which_flavour == "xxx":
            break
        # use icing ordering function to get icing
        icing_order()

        # use yes/no function to ask if user wants toppings
        want_toppings = yes_no("\nWould you like any toppings? ")

        # use topping function if they want toppings
        if want_toppings == "yes" or want_toppings == "y":
            which_toppings()
        else:
            current_order["toppings"] = []

        # send current order to order list
        order_list.append(current_order)

    # loop to get user information for the order
    while True:
        # gets users name
        while True:
            name = not_blank("\nPlease enter a name for the order: ").capitalize()
            if name in name_list:
                print("Sorry, there is already an order under this name. Please try again.")
            else:
                name_list.append(name)
                break
        # asks if user wants pickup or delivery
        order_option = pickup_delivery("\nWould you like pickup or delivery? ")
        if order_option == "pickup":
            break
        elif order_option == "delivery":
            # use function to get the address
            address = get_address()
            phone_number = num_check("\nWhat is your phone number? ", "Please enter a valid phone number")
            break

    # calculates total price and adds delivery fee if chosen
    total_price, individual_prices = calculate_total(order_list)
    if order_option == "delivery":
        total_price += 5

    # prints order summary for the user and total price
    to_write = f"\nOrder Summary for {name}\n"
    for idx, (order, prices) in enumerate(zip(order_list, individual_prices), start=1):
        # print each order and order number
        to_write += f"Order {idx}:\n"
        # writes cake and icing chosen
        to_write += f"  Cake: {order['cake'].capitalize()} (${prices['cake']})\n"
        to_write += f"  Icing: {order['icing'].capitalize()} (${prices['icing']})\n"
        # check if toppings were picked, says none if they weren't
        if order['toppings']:
            to_write += f"  Toppings: {', '.join(topping.capitalize() for topping in order['toppings'])} (${prices['toppings']})\n"
        else:
            to_write += "  Toppings: None\n"
        to_write += "\n"

    if order_option == "delivery":
        to_write += "\nDelivery Fee: $5\n"
        to_write += f"Being Delivered to {address}\nPhone Number: {phone_number}"
    else:
        to_write += "\nOrder is being picked up, no extra charge"

    # sends total price to to_write
    to_write += f"\nTotal Price: ${total_price}\n"

    print(to_write)

    while True:
        cancel_confirm = input("Please confirm or cancel your order: ").lower()
        if cancel_confirm == "cancel":
            print("Your order has been cancelled")
            exit()
        elif cancel_confirm == "confirm":
            break
        else:
            print("Please type either confirm or cancel")

    # gets payment method using function
    while True:
        payment_method = cash_credit("\nHow would you like to pay? (cash or credit) ")

        if payment_method == "cash" or payment_method == "credit":
            break

    # write to file
    file_name = "{}'s Order.txt".format(name)
    with open(file_name, "w") as text_file:
        text_file.write(to_write)

    another_order = yes_no("\nWould you like to place another order? ")
    if another_order == "yes":
        order_list = []  # Clear the order list for the new order
        continue
    else:
        print("\nThank you for ordering with us! Your order is being processed now.")
        break
