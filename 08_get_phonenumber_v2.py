def num_check(question, error):
    valid = False
    while not valid:

        response = input(question)

        if response.isdigit():
            print(response)
        else:
            print(error)


phone_number = num_check("What is your phone number? ", "Please enter a valid phone number")

print(phone_number)
