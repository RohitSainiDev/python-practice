principle = 0
rate = 0
time = 0

while True:
    principle = float(input("Enter principle: "))
    if principle < 0:
        print("Enter a value >= 0")
    else:
        break

while True:
    rate = float(input("Enter rate: "))
    if rate < 0:
        print("Enter a value >= 0")
    else:
        break

while True:
    time = float(input("Enter time: "))
    if time < 0:
        print("Enter a value >= 0")
    else:
        break

total = principle * pow((1 + rate / 100), time)
print(f"Total after {time} year/s: ₹{total:.2f}")
