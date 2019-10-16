def love_pizza():
    print("I love pizza")
    pass


def absolute_value(number):
    if number >= 0:
        return number
    else:
        return -number


def shutdown(yn):
    if yn.lower()=="y":
        return "Closing files and shutdown"
    elif yn.lower()=="n":
        return "Shutdown terminated"
    else:
        return "Check your response"


def calculator(x,y):
    return x*y+2


def factorial(count):
    if count==0:
        return 1
    elif count<0:
        return "Number can NOT be less than zero"
    else:
        return count*factorial(count-1)


def members_total(n):
    return n*3


def org_total(m):
    return members_total(m)+5
