import math

gamer = input("enter a number ")
try:
    x = float(gamer)
    print(x)
except TypeError:
    print("\nthis is the wrong oporation ")
except ValueError:
    print("\nthis is not a number")