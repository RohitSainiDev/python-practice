fruits = [
    "apple",
    "banana",
    "orange",
    "coconut",
]

print(fruits)

print(fruits[0])  # We can use all indexing operations here [start:end:step]

for fruit in fruits:
    print(fruit)

fruits[0] = "pineapple"
fruits.append("pineapple")
fruits.remove("apple")
fruits.insert(0, "pineapple")
fruits.sort()
fruits.reverse()
fruits.clear()
print(fruits.index("apple"))
print(fruits.count("banana"))

print(dir(fruits))
print(help(fruits))

print(fruits)
