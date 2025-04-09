temp = 25
is_raining = False
is_sunny = True

if temp > 35 or temp < 0 or is_raining:
    print("The outdoor event is cancelled ❌")
else: 
    print("The outdoor event is scheduled ✅")

if temp > 28 and is_sunny:
    print("It's HOT outside 🥵")
    print("It is sunny ☀️")
elif temp <= 0 and is_sunny:
    print("It's COLD outside 🥶")
    print("It is sunny ☀️")
elif 28 > temp > 0 and is_sunny:
    print("It;s warm outside 😊")
    print("It is sunny ☀️")
elif temp > 28 and not is_sunny:
    print("It's HOT outside 🥵")
    print("It is cloudy ☁️")
elif temp <= 0 and not is_sunny:
    print("It's COLD outside 🥶")
    print("It is cloudy ☁️")
elif 28 > temp > 0 and not is_sunny:
    print("It;s warm outside 😊")
    print("It is cloudy ☁️")