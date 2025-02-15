import random

temper = random.randint(1,400)

if temper > 100:
    print("Temperature above boiling point")

    if temper > 320:
        print("Temperature above smoke point")

elif temper < 100:
    print("The temperature is not very high")

