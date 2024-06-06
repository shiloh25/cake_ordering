def pickup_delivery():

    while True:
        response = input("Would you like pickup or delivery? ").lower()

        if response == "pickup" or response == "delivery":
            print("You have chosen {}".format(response))
            return response

        else:
            print("Please choose either pickup or delivery")



pickup_delivery()