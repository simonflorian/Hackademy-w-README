def add_num(a,b):
    c = a+b
    return c



print(add_num(6,5))

def hello(name):
    print("hello " + name)

hello("simon")

import math

def circle_area(radius):
    circle_area = radius**2 * math.pi
    return circle_area

r = float(input("Give me a radius, please:"))
z = circle_area(r)
print(z)

import datetime
now = datetime.datetime.now()

print(now)
print(now.year)
print(now.month)
print(now.day)

