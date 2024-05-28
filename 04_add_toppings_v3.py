# functions go here
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


toppings_list = ["chocolates", "strawberries", "raspberries", "coconut",
                 "blueberries", "oranges", "lemons", "sprinkles", "lollies", "caramel"]

while True:
    topping1 = which_toppings("What is the first topping you would like? ")
    if topping1 is None:
        break

    topping2 = which_toppings("What is the second topping you would like? ")
    if topping2 is None:
        break

    topping3 = which_toppings("What is the third topping you would like? ")
    if topping3 is None:
        break




