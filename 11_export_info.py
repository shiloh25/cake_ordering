to_write = "\nOrder Summary:"
for idx, order in enumerate(order_list, start=1):
    print(f"Order {idx}:")
    print(f"  Cake: {order['cake'].capitalize()}")
    print(f"  Icing: {order['icing'].capitalize()}")
    if order['toppings']:
        print(f"  Toppings: {', '.join(topping.capitalize() for topping in order['toppings'])}")
        print()
    else:
        print("  Toppings: None")
        print()
if order_option == "delivery":
    print("Delivery Fee: $5")
print()

print("Total Price: ${}".format(total_price))
print()

# write to file
# create file to hold data (add .txt extention)
file_name = "order.txt"
text_file = open(file_name, "w+")

# heading
for item in to_write:
    text_file.write(item)
    text_file.write("\n\n")

text_file.write(variable_txt)

# close file
text_file.close()

# print stuff
for item in to_write:
    print(item)
    print()