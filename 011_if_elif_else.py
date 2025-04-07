age = int(input("Enter your age: "))

if age >=100:
    print("You are a centenarian!")
elif age >= 18:
    print("You are an adult!")
elif age >= 13:
    print("You are a teenager!")
elif age >= 5:
    print("You are a child!")
elif age >= 0:
    print("You are a toddler!")
else:
    print("Invalid age entered!")