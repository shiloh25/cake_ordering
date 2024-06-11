import pandas


def menu():
    print(cake_frame)



data = {
    "cakes": ["chocolate", "strawberry", "vanilla", "lemon", "banana",
             "carrot", "pistachio", "coffee", "raspberry", "coconut", "funfetti"],
    "price": [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110]
}


cake_frame = pandas.DataFrame(data)
cake_frame = cake_frame.set_index("cakes")


menu()

