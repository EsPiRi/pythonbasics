my_var = 10
my_var = my_var + 3
print(my_var)
my_var = "yellow"
print(my_var)
string1 = 'i am enclosed in single quotes.'  # using single quotes in string
string2 = "i am enclosed in double quotes."  # using double quotes in string
print(string1 + "\n" + string2)

string3 = 'it doesn\'t look good at all.'  # using single quotes in strings but with an extra
print(string3)
txt = """He said:"you should get something" """
print(txt)

s = "Hello python"  # getting the character of the string
print(s[0])
print(s[len(s) - 1])
print(s[-2])

# concatenating strings
string4 = "hello " + "world"
print(string4)

# repeating strings
string5 = "**/\**" * 5
print(string5)

# size of string
print(len("hello world"))

# slicing strings
string6 = "program"
print(string6[3:5])  # gr
print(string6[3:6])  # gra
print(string6[4:])  # ram
print(string6[:4])  # prog

# lowering and uppering strings
string7 = "Grand River"
print(string7.lower())
print(string7.upper())

# str() method: converts the number into strings
pi = 3.1416
print(pi + 5)  # concatenating only works with the same type of variables
print(str(pi) + "5")

# octal, binary and hexadecimal numbers
numOctal = 0o10
numHex = 0xABC
numBin = 0b01101
print(str(numOctal) + " " + str(numHex) + " " + str(numBin))

# converting numbers into binary octal and hexadecimal
num1 = 123
print(bin(num1), oct(num1), hex(num1))

# complex numbers can be held in python
comp1 = 3 + 5j
comp2 = -3 - 4j
print(comp1 + comp2)

# date and time in python
from datetime import datetime

print(datetime.now())
from time import strftime

print(strftime("%Y-%m-%d %H:%M:%S"))
