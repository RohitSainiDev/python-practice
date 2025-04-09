num = 5
var_1 = 6
var_2 = 7
age = 30
temp = 20
user_role = "admin"



print("Positive" if num > 0 else "Negative")
print("Even" if num % 2 == 0 else "Odd")

max_num = var_1 if var_1 > var_2 else var_2
min_num = var_1 if var_1 < var_2 else var_2
print(max_num)
print(min_num)

status = "Adult" if age >= 18 else "Child"
print(status)

weather = "Hot" if temp >=20 else "Cold"
print(weather)

access_level = "Full Access" if user_role == "admin" else "Limited Access"
print(access_level)
 