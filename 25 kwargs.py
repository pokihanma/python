# kwargs = parameter that pack all the arguments in a dictionary
#          useful so that a function can accept a varying amount of keyword argument


def hello(**kwargs):
    print("hiii ", end=" ")
    for key, value in kwargs.items():
        print(value, end=" ")


hello(first="hello", sec="poki", last="hanma")
