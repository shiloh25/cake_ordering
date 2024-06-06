def icing_order():
    while True:

        icing_flavour = input("What flavour icing would you like? ").lower()

        if icing_flavour in icing_list:
            print("You have chosen {} icing".format(icing_flavour))
            break

        elif icing_flavour == "none":
            print("You have chosen no icing")
            break
        elif icing_flavour == "menu":
            menu()
            continue
        else:
            print("Please choose an option from the menu or none\n")


icing_list = ["chocolate", "strawberry", "vanilla", "lemon", "coffee",
              "raspberry", "coconut", "caramel", "blueberry", "orange"]
icing_order()