items = []
prices = []
total = 0

while True:
    item = input("Enter an item to cart (q to quit): ")
    if item.lower() == "q":
        break
    else:
        price = float(input(f"Enter the per-unit price of {item}: ₹"))
        items.append(item)
        prices.append(price)

print("-----Your Cart-----")

for item in items:
    print(item, end=" ")

for price in prices:
    total += price

print()
print(f"Your total is: ₹{total}")
