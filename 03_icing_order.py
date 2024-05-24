icing_list = ["chocolate", "strawberry", "vanilla", "lemon", "coffee",
             "raspberry", "coconut", "caramel", "blueberry", "orange"]

while True:

    icing_flavour = input("What flavour icing would you like? ").lower()

    if icing_flavour in icing_list:
        print("You have chosen {} icing".format(icing_flavour))
        print("program continues...\n")

    elif icing_flavour == "none":
        print("You have chosen no icing")
        print("program continues...\n")

    else:
        print("Please choose an option from the menu or none\n")
