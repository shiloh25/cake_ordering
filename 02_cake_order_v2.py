def cake_order():
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


cake_list = ["chocolate", "strawberry", "vanilla", "lemon", "banana",
             "carrot", "pistachio", "coffee", "raspberry", "coconut", "funfetti"]
cake_order()
