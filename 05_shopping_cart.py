# This program calculates the total cost of items in a shopping cart.

item = input("What would you like to buy?: ")
price = float(input("Enter price of one article: "))
quantity = int(input(f"How many {item} you want?: "))
total = price * quantity

print(f"{quantity} {item} will cost you ₹{total}")