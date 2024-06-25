# functions go here
def cash_credit(question):

    while True:
        response = input(question).lower()

        if response == "cash" or response == "ca":
            return "cash"

        elif response == "credit" or response == "cr":
            return "credit"

        else:
            print("Please choose a valid payment method")


# main routine goes here
while True:
    payment_method = cash_credit("How would you like to pay? (cash or credit) ")

    print("You chose {}".format(payment_method))

    print("program continues...")
    print()
