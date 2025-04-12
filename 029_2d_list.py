foods = ["apple", "banana", "coconut"]
beverages = ["tea", "coffee"]
vegetables = ["carrot", "potato", "spinach"]

# cart = [foods, beverages, vegetables]
cart = [
    ["apple", "banana", " coconut"],
    ["tea", "coffee"],
    ["carrot", "potato", "spinach"],
]

print(cart)

print(cart[0])
print(cart[0][1])


for collection in cart:
    for item in collection:
        print(item, end=" ")
    print()
