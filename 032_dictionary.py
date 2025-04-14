capitals = {
    "USA": "Washington D.C.",
    "India": "New Delhi",
    "China": "Beijing",
    "Russia": "Moscow",
}
print(capitals)
print(capitals.get("USA"))

# Check if a certain value is present in a dictionary
if capitals.get("Japan"):
    print("That capital exists.")
else:
    print("That capital doesn't exist.")

capitals.update({"Japan": "Tokyo"})

for capital in capitals:
    print(capital, end=" ")

capitals.pop("China")
capitals.popitem()
# capitals.clear()

print(capitals)

for key in capitals.keys():
    print(key, end=" ")

print()

for value in capitals.values():
    print(value)

for key, value in capitals.items():
    print(f"{key}:{value}")
