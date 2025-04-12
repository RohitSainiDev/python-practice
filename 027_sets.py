fruits = {"apple", "banana", "orange", "coconut"}
print(fruits)
# print(fruits[0])  # Error

print(len(fruits))

for fruit in fruits:
    print(fruit, end=" ")

print("pineapple" in fruits)
fruits.add("pineapple")
fruits.remove("apple")
fruits.pop()
fruits.clear()

print(fruits)
