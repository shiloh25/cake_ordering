while True:
    cancel_confirm = input("Please confirm or cancel your order: ").lower()
    if cancel_confirm == "cancel":
        break
    elif cancel_confirm == "confirm":
        break
    else:
        print("Please type either confirm or cancel")
