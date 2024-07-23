import pandas as pd
from tabulate import tabulate


def menu():
    # Format the prices to include dollar signs
    formatted_cake_price = [f'${price}' for price in cake_price]
    formatted_icing_price = [f'${price}' for price in icing_price]
    formatted_topping_price = [f'${price}' for price in topping_price]

    cake = pd.DataFrame(list(zip(cake_list, formatted_cake_price)),
                        columns=['Cakes', 'Price'])
    print(tabulate(cake, showindex=False, headers=cake.columns))
    print()
    icing = pd.DataFrame(list(zip(icing_list, formatted_icing_price)),
                         columns=['Icing', 'Price'])
    print(tabulate(icing, showindex=False, headers=icing.columns))
    print()
    topping = pd.DataFrame(list(zip(toppings_list, formatted_topping_price)),
                           columns=['Toppings', 'Price'])
    print(tabulate(topping, showindex=False, headers=topping.columns))


cake_list = ["Chocolate", "Strawberry", "Vanilla", "Lemon", "Banana",
             "Carrot", "Pistachio", "Coffee", "Raspberry", "Coconut", "Funfetti"]
cake_price = [8, 8, 8, 8, 8, 8, 10, 10, 10, 10, 6]

icing_list = ["Chocolate", "Strawberry", "Vanilla", "Lemon", "Coffee",
              "Raspberry", "Coconut", "Caramel", "Blueberry", "Orange"]
icing_price = [2, 2, 2, 2, 3, 3, 3, 3, 3, 3]

toppings_list = ["Chocolates", "Strawberries", "Raspberries", "Coconut",
                 "Blueberries", "Oranges", "Lemons", "Sprinkles", "Lollies", "caramel"]
topping_price = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2]

menu()

