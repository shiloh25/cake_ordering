# functions go here
def yes_no(question):

    while True:
        response = input(question).lower()

        if response == "yes" or response == "y":
            return "yes"

        elif response == "no" or response == "n":
            return "no"

        else:
            print("please enter yes or no")


# main routine goes here
while True:
    want_toppings = yes_no("Would you like any toppings? ")

    if want_toppings == "yes" or want_toppings == "y":
        print("ask which topping here")

    print("program continues...")
    print()