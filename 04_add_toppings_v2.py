toppings_list = ["chocolates", "strawberries", "raspberries", "coconut",
                 "blueberries", "oranges", "lemons", "sprinkles", "lollies", "caramel"]
max_toppings = 3
current_toppings = 0

while current_toppings < max_toppings:
    topping_one = input("What is the first topping you would like? ")

    if topping_one in toppings_list:
        print("You have chosen {}".format(topping_one))
        current_toppings += 1
        pass

    elif topping_one == "xxx":
        print("You have chosen no further toppings\n")
        break

    else:
        print("Please choose a topping from the menu or xxx for no more toppings\n")
        pass

    topping_two = input("What is the second topping you would like? ")

    if topping_two in toppings_list:
        print("You have chosen {}".format(topping_two))
        current_toppings += 1
        pass

    elif topping_two == "xxx":
        print("You have chosen no further toppings\n")
        break

    else:
        print("Please choose a topping from the menu or xxx for no more toppings\n")

    topping_three = input("What is the third topping you would like? ")

    if topping_three in toppings_list:
        print("You have chosen {}".format(topping_three))
        current_toppings += 1
        continue

    elif topping_three == "xxx":
        print("You have chosen no further toppings\n")
        break

    else:
        print("Please choose a topping from the menu or xxx for no more toppings\n")
        pass
