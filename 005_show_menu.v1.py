# functions go here
def menu():
    print("***** Menu *****\n")
    print("***** Cake Flavours *****\n")
    for item in cake_list:
        print(item.capitalize())

    print("\n***** Icing Flavours *****\n")
    for item in icing_list:
        print(item.capitalize())

    print("\n***** Toppings *****\n")
    for item in toppings_list:
        print(item.capitalize())


cake_list = ["chocolate", "strawberry", "vanilla", "lemon", "banana",
             "carrot", "pistachio", "coffee", "raspberry", "coconut", "funfetti"]
icing_list = ["chocolate", "strawberry", "vanilla", "lemon", "coffee",
             "raspberry", "coconut", "caramel", "blueberry", "orange"]
toppings_list = ["chocolates", "strawberries", "raspberries", "coconut",
                 "blueberries", "oranges", "lemons", "sprinkles", "lollies", "caramel"]

menu()