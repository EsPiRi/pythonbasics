from conditional import your_choice
from myFunctions import *

a = range(5)
print(a)
print(list(range(5)))
print(list(range(4, 88, 7)))
print(abs(-5), abs(3 + 4j))
print(max(9, 12, 6, 15), max(-2, -7, -35, -4))
print(min(9, 12, 6, 15), min(-2, -7, -35, -4))
print(type(a))
print(type("string"))
print(type(5))
print(type(2 + 3j))

# name=input("May i know your name? ")
# print("It's a pleasure to meet you "+name+"!")
# age=input("Your age, please? ")
# print("So you are "+age+" years old, "+name+"!")

print(your_choice(6))
print(your_choice(3))
print(your_choice(1))
print(your_choice(0))
print(absolute_value(-5))
print(absolute_value(10))
print(love_pizza())

print(shutdown("y"))
print(shutdown("n"))
print(shutdown("xx"))

print("2*6+2=", calculator(2, 6), "3*7+2=", calculator(3, 7))

print(factorial(-5))

print(org_total(2))
print(org_total(5))
print(org_total(10))
