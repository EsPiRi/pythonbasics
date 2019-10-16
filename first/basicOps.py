# arithmetic ops
a = 5 + 2  # addition
b = 3 - 4  # subtraction
c = 4 * 5  # multiplication
d = 7 / 6  # division
e = 2 ** 5  # exponential
f = 22 % 8  # modulus
g = 21 // 4  # floor division means removing the decimal numbers after quotient
print(a, b, c, d, e, f, g)
meal = 65.50
tax = 6.6 / 100
tip = 20 / 100
meal = meal + meal * tax
total = meal + meal * tip
print("total: " + str(total))
boolA = a == b
boolB = a > b
print((not a == b and a > b) or (a == b and not a > b))
