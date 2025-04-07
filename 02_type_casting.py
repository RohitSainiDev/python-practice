# Type casting is the process of converting a variable from one data type to another.
# In Python, this can be done using built-in functions like int(), float(), str(), and bool().

name = "Visitor"
age = 27
cgpa = 7.56
like_computer_science = True


# Type casting examples
cgpa = int(cgpa)  # Convert float to int
print(cgpa)

age = float(age)  # Convert int to float
print(age)

age = str(age)  # Convert int to string
print(type(age))  # Check the type of age after conversion
print(age+"1")  # Concatenate string with int (after conversion to string)

name = bool(name)  # Convert string to boolean (non-empty string is True)
print(name)

