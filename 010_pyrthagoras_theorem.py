import math

perpendicular = float(input("Enter length of the perpendicular of the triangle: "))
base = float(input("Enter length of the base of the triangle: "))

hypotenuse = math.sqrt(pow(perpendicular, 2) + pow(base, 2))
print(f"The length of the hypotenuse is: {round(hypotenuse, 2)} unit")

