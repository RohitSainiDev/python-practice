# The input() function is used to take input from the user. It returns the input as a string.

name = input("May I know your name?: ")

age = input("Enter your age: ")
print(type(age))
age = int(age) # We can combine type casting and taking user input in one line:
#                   age = int(input("Enter your age: "))
age = age+1

print(f"Hello, {name}!")
print(f"Next year you'll be {age} years old.")