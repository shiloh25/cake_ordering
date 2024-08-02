def get_address():
    while True:
        address = input("Where would you like the order delivered? ")
        number = any(map(str.isdigit, address))
        string = any(map(str.isalpha, address))
        if number == True and string == True:
            print("program continues...")
        else:
            print("please enter a valid address")


get_address()
