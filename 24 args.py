# args = parameter that will pack all arguments into a tuble
#        useful so that function can accept a varying amount of arguments


"""#normal function : 
def add(num1, num2):
    sum = num1 + num2
    return sum


print(add(1, 2))
"""


def add(*args):
    sum = 0
    for i in args:
        sum += i
    return sum


# its works like tubles so we cant insert any values but by inserting all vaues in a list we can insert new values in the tuble


print(add(1, 2, 3, 4, 5, 6))
