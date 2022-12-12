from ast import arguments


"""Higher order function : functions that accept a function as a argument
    or 
    
returns a function(in python functions can also treated as arguments)"""

def loud(text):
    return text.upper()

def quite(text):
    return text.lower()

def hello(func):#in this place the func is treated as argument and implements the called functions in the given value
    
    text = func("hello")
    print(text)
    
hello(loud)#function calls a function
hello(quit)