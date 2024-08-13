import pandas as pd
from tabulate import tabulate
import os


# functions go here
# function that shows the menu
def menu():
    print("\n***** Menu *****")
    # Format the prices to include dollar signs
    formatted_cake_price = [f'${price}' for price in cake_price]
    formatted_icing_price = [f'${price}' for price in icing_price]
    formatted_topping_price = [f'${price}' for price in topping_price]

    cake = pd.DataFrame(list(zip(cake_list, formatted_cake_price)),
                        columns=['Cakes', 'Price'])
    print(tabulate(cake, showindex=False, headers=cake.columns))
    print()
    icing = pd.DataFrame(list(zip(icing_list, formatted_icing_price)),
                         columns=['Icing', 'Price'])
    print(tabulate(icing, showindex=False, headers=icing.columns))
    print()
    topping = pd.DataFrame(list(zip(toppings_list, formatted_topping_price)),
                           columns=['Toppings', 'Price'])
    print(tabulate(topping, showindex=False, headers=topping.columns))
    print()


# Generalized function to check that an input is within a set of valid options
def get_valid_input(question, valid_responses, error_message="Please enter a valid response"):
    while True:
        response = input(question).lower()
        if response in valid_responses:
            return response
        else:
            print(error_message)


# yes_no using get_valid_input to check the user answers yes or no
def yes_no(question):
    return get_valid_input(question, ["yes", "y", "no", "n"], "Please enter yes or no")


# cash_credit using get_valid_input to check the user answers cash or credit
def cash_credit(question):
    return get_valid_input(question, ["cash", "ca", "credit", "cr"], "Please choose a valid payment method")


# pickup_delivery using get_valid_input to check the user answers pickup or delivery
def pickup_delivery(question):
    return get_valid_input(question, ["pickup", "delivery"], "Please choose either pickup or delivery")


# confirm_cancel using get_valid_input to check the user answer cancel or confirm
def confirm_cancel(question):
    return get_valid_input(question, ["confirm", "cancel"], "Please type either confirm or cancel")


# checks that an input is not blank
def not_blank(question):
    while True:
        response = input(question)

        # if the response is blank, outputs error
        if response == "":
            print("Sorry this can't be blank. Please try again")
        else:
            return response


# function to count the number of cakes
def cake_counter():
    cake_counter.counter += 1
    return cake_counter.counter


# cake ordering function
def cake_order(question):
    while True:
        cake_flavour = input(question).capitalize()

        if cake_flavour == "Xxx" and cake_counter.counter == 0:
            print("You need to order at least one cake.\n")
        elif cake_flavour in cake_list:
            print("You have chosen {}".format(cake_flavour))
            cake_counter()
            topping_counter.counter = 1
            current_order["cake"] = cake_flavour
            break
        elif cake_flavour == "Menu":
            menu()
            continue
        elif cake_flavour == "Xxx":
            return cake_flavour
        else:
            print("Please choose an option from the menu\n")


# icing ordering function
def icing_order():
    while True:
        icing_flavour = input("\nWhat flavour icing would you like? ").capitalize()

        if icing_flavour in icing_list:
            print("You have chosen {} icing".format(icing_flavour))
            current_order["icing"] = icing_flavour
            break

        elif icing_flavour == "None":
            print("You have chosen no icing")
            current_order["icing"] = "none"
            break
        elif icing_flavour == "Menu":
            menu()
            continue
        else:
            print("Please choose an option from the menu or none")


# topping ordering function
def which_toppings():
    current_order["toppings"] = []
    while topping_counter.counter <= 3:
        response = input("\nTopping {}: ".format(topping_counter.counter)).capitalize()
        if response in toppings_list:
            topping_counter()
            print("You have chosen {}".format(response))
            current_order["toppings"].append(response)
            continue

        elif response == "Xxx":
            print("You have chosen no further toppings")
            break

        elif response == "Menu":
            menu()

        else:
            print("Please choose an item from the menu or xxx for no more toppings")


# function to count number of toppings
def topping_counter():
    topping_counter.counter += 1
    return topping_counter.counter


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


# function to check that an input is only numbers, greater than 7 and less than 15
def num_check(question, error):
    while True:
        response = input(question)

        if response.isdigit() and 7 <= len(response) <= 15:
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


# function to load names from file
def load_names(filename):
    if os.path.exists(filename):
        with open(filename, "r") as file:
            return [line.strip() for line in file.readlines()]
    return []


# function to save names to file
def save_names(filename, names):
    with open(filename, "w") as file:
        for name in names:
            file.write(f"{name}\n")


# main routine goes here
# menu and price lists
cake_list = ["Chocolate", "Strawberry", "Vanilla", "Lemon", "Banana",
             "Carrot", "Pistachio", "Coffee", "Raspberry", "Coconut", "Funfetti"]
cake_price = [8, 8, 8, 8, 8, 8, 10, 10, 10, 10, 6]

icing_list = ["Chocolate", "Strawberry", "Vanilla", "Lemon", "Coffee",
              "Raspberry", "Coconut", "Caramel", "Blueberry", "Orange"]
icing_price = [2, 2, 2, 2, 3, 3, 3, 3, 3, 3]

toppings_list = ["Chocolates", "Strawberries", "Raspberries", "Coconut",
                 "Blueberries", "Oranges", "Lemons", "Sprinkles", "Lollies", "Caramel"]
topping_price = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2]

# load name list from file
name_list = load_names("name_list.txt")

# topping counter
topping_counter.counter = 1

# order list and dictionary
order_list = []
current_order = []

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
        # use cake ordering function to get cake flavour
        print("\nCake Number {}".format(cake_counter.counter + 1))
        which_flavour = cake_order("What flavour cake would you like? ")
        if which_flavour == "Xxx" and cake_counter.counter > 0:
            break

        # use icing ordering function to get icing flavour
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
            # tells the user if there is already an order under that name and asks them to try again
            if name in name_list:
                print("Sorry, there is already an order under this name. Please try again.")
            else:
                name_list.append(name)
                break
        # asks if user wants pickup or delivery
        order_option = pickup_delivery("\nWould you like pickup or delivery? ")
        if order_option == "pickup":
            # gets user phone number
            phone_number = num_check("\nWhat is your phone number? ", "Please enter a valid phone number")
            break
        elif order_option == "delivery":
            # use functions to get the address and phone number
            address = get_address()
            phone_number = num_check("\nWhat is your phone number? ", "Please enter a valid phone number")
            break

    # gets payment method using function
    while True:
        payment_method = cash_credit("\nWould you like to pay with cash or credit (15% surcharge for credit) ")

        if payment_method == "cash" or payment_method == "credit" or payment_method == "ca" or payment_method == "cr":
            break

    # calculates total price and adds delivery fee if chosen
    total_price, individual_prices = calculate_total(order_list)
    if order_option == "delivery":
        total_price += 5
    # applies a 15% surcharge if credit is chosen
    if payment_method == "credit" or payment_method == "cr":
        total_price *= 1.15

    # prints order summary for the user and total price
    to_write = f"\n*** Order Summary for {name} ***\n"
    for idx, (order, prices) in enumerate(zip(order_list, individual_prices), start=1):
        # print each order and order number
        to_write += f"Order {idx}:\n"
        # writes cake and icing chosen
        to_write += f"  Cake: {order['cake'].capitalize()} (${prices['cake']})\n"
        to_write += f"  Icing: {order['icing'].capitalize()} (${prices['icing']})\n"
        # check if toppings were picked, says none if they weren't
        if order['toppings']:
            to_write += f"  Toppings: {', '.join(topping.capitalize() for topping in order['toppings'])}" \
                        f" (${prices['toppings']})\n"
        else:
            to_write += "  Toppings: None\n"
        to_write += "\n"

    # if the user chooses delivery, displays delivery information
    if order_option == "delivery":
        to_write += "\n*** Customer Information ***\nDelivery Fee: $5\n"
        to_write += f"Being Delivered to {address}\nPhone Number: {phone_number}"
    # if the user chooses pickup, displays pickup information
    else:
        to_write += f"\n*** Customer Information ***\nPhone Number: {phone_number}\n" \
                    f"Order is being picked up, no extra charge"

    # sends total price to to_write
    to_write += f"\nTotal Price: ${total_price:.2f}\n"

    # prints order info here
    print(to_write)

    # asks the user to confirm or cancel their order
    while True:
        cancel_confirm = input("Please confirm or cancel your order: ").lower()
        # cancels order if user chooses cancel
        if cancel_confirm == "cancel":
            print("Your order has been cancelled")
            exit()
        # continues if user chooses confirm
        elif cancel_confirm == "confirm":
            break
        else:
            print("Please type either confirm or cancel")

    # write to file
    file_name = "{}'s Order.txt".format(name)
    with open(file_name, "w") as text_file:
        text_file.write(to_write)

    # asks the user if they would like to place another order
    another_order = yes_no("\nWould you like to place another order? ")
    if another_order == "yes":
        order_list = []  # Clear the order list for the new order
        continue
    else:
        # Save the updated name list to the file
        save_names("name_list.txt", name_list)
        print("\nThank you for ordering with us! Your order is being processed now.")
        break
