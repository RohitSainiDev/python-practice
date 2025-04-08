unit = input(" Choose the input temperature unit Celcius or Fahrenheit(C/F): ")
temp = float(input("Enter the temperature: "))

if unit == "C":
    temp = round((temp * 9) / 5 + 32, 2)
    print(f"Temperature in Fahrenheit: {temp}")
elif unit == "F":
    temp = round((temp - 32) * 5 / 9, 2)
    print(f"Temperature in Celcius: {temp}")

else:
    print("Invalid temperature unit!")