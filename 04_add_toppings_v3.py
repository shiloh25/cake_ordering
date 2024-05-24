# functions go here
def which_toppings(question):

    while True:
        response = input(question).lower()

        if response in toppings_list:
            print("You have chosen {}".format(response))
            return response

        else:
            print("Please choose an item from the menu or xxx for no more toppings")


toppings_list = ["chocolates", "strawberries", "raspberries", "coconut",
                 "blueberries", "oranges", "lemons", "sprinkles", "lollies", "caramel"]

while True:
    topping = which_toppings("What toppings would you like? ")

    if topping == "xxx":
        print("You have chosen no further toppings")
        break


