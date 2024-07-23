while True:
    cancel_confirm = input("Please confirm or cancel your order: ").lower()
    if cancel_confirm == "cancel":
        print("Your order has been cancelled\n")
        continue
    elif cancel_confirm == "confirm":
        print("Thank you for confirming your order\n")
        continue
    else:
        print("Please type either confirm or cancel\n")
