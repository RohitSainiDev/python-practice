name = input("Enter your full name: ")
mobile_num = input("Enter your mobile number: ")

print(len(name))

result = name.find(" ") # Returns index
print(result)

result = name.find("i")
print(result)

result = name.rfind("i")
print(result)

name = name.capitalize()
print(name)

name = name.upper()
print(name)

name = name.lower()
print(name)

result = name.isdigit()
print(result)

result = mobile_num.count("+")
print(result)


mobile_num = mobile_num.replace("9", "8")
print(mobile_num)

# For the list of all such functions
print(help(str))