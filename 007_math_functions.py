# Python has a built-in math module that provides various mathematical functions.
import math

int_num = 5
float_num = 5.5
negative_int =-4

print(f"Absolute function: abs({negative_int}) = {abs(negative_int)}")
print(f"Round function: round({float_num}) = {round(float_num)}")
print(f"Power funtion: pow({int_num},2) = {pow(int_num, 2)}")
print(f"Max function: max({int_num}, {float_num},{negative_int}) = {max(int_num, float_num,negative_int)}")
print(f"Min function: min({int_num}, {float_num},{negative_int}) = {min(int_num, float_num,negative_int)}")
print(f"Pi = {math.pi}")
print(f"E = {math.e}")
print(f"Sqrt function: math.sqrt({int_num}) = {math.sqrt(int_num)}")
print(f"Floor function: math.floor({float_num})= {math.floor(float_num)}")
print(f"Ceil function: math.ceil({float_num}) = {math.ceil(float_num)}")
