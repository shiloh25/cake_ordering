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
    want_instructions = yes_no("Do you want to read the menu? ")

    if want_instructions == "yes" or want_instructions == "y":
        print("menu go here")

    print("program continues...")
    print()

