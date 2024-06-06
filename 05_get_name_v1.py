def not_blank(question):

    while True:
        response = input(question)

        # if the response is blank, outputs error
        if response == "":
            print("Sorry this can't be blank. Please try again")
        else:
            return response


while True:
    name = not_blank("Please enter a name for the order: ")
    print(name)