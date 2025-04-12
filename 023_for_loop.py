for x in range(1, 11):
    print(x, end="")

print()

for x in reversed(range(1, 11)):
    print(x, end="")

print()

for x in range(1, 11, 2):
    print(x, end="")

print()

ph_num = "+91-123456789"
for x in ph_num:
    print(x, end="")

print()

for x in range(1, 21):
    if x == 13:
        continue
    else:
        print(x, end="")

print()

for x in range(1, 21):
    if x == 13:
        break
    else:
        print(x, end="")
