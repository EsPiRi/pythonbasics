pizza = ["NY Style pizza", "pan pizza", "thin pizza", "crust pizza"]
for choice2 in pizza:
    if choice2 == "pan pizza":
        print("pay $16 pls")

    print("cheesy ", choice2)
else:
    print("cheesy pan pizza is my favorite!")

print("finally, im full")

x = 50

total = 0
for number in range(1, x + 1):
    total += number
print("sum of 1 until {0}: {1}".format(x, total))

counter = 0
while counter < 10:
    print("the count is: ", counter)
    counter += 1

print("done")
