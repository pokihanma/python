"""
keyword arguments = Keyword arguments (or named arguments) are values that, when passed into a function, are identifiable by specific parameter names. A keyword argument is preceded by a parameter and the assignment operator, = . Keyword arguments can be likened to dictionaries in that they map a value to a keyword."""


def hello(first, middle, last):
    print("hello ", first, middle, last)


hello(first="poki", last="hanma", middle="s")
