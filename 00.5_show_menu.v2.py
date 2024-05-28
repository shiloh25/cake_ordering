import pandas as pd


data = {
    "cakes": ["chocolate", "strawberry", "vanilla", "lemon", "banana",
             "carrot", "pistachio", "coffee", "raspberry", "coconut", "funfetti"],
    "price": [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110]
}
df = pd.DataFrame(data)

print(df)

