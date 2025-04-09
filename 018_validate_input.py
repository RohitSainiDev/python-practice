username = input("Enter a username: ")

if len(username) > 12:
    print("Username can't have more than 12 characters")
elif not(username.find(" ")== -1):
    print("Username can't contain spaces")
elif not(username.isalpha()):
    print("Username should only contain alphabets")
else:
    print(f"Welcome {username}")

