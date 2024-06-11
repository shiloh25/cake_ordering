def which_toppings():

    while topping_counter.counter <= 10:
        response = input("Topping {}: ".format(topping_counter.counter)).lower()
        if response in toppings_list:
            topping_counter()
            print("You have chosen {}".format(response))
            continue

        elif response == "xxx":
            print("You have chosen no further toppings")
            break

        elif response == "menu":
            menu()

        else:
            print("Please choose an item from the menu or xxx for no more toppings\n")


def topping_counter():
    topping_counter.counter += 1
    return topping_counter.counter


topping_counter.counter = 1
toppings_list = ["chocolates", "strawberries", "raspberries", "coconut",
                 "blueberries", "oranges", "lemons", "sprinkles", "lollies", "caramel"]

which_toppings()
