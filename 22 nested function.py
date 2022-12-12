"""nested function calls = A function defined inside another function is called a nested function. Nested functions can access variables of the enclosing scope. In Python, these non-local variables are read-only by default and we must declare them explicitly as non-local (using nonlocal keyword) in order to modify them."""
"""
num = input("enter a whole positive number : ")
num = float(num)
print(num)
num = abs(num)
print(num)

num = round(num)
print(num)"""

print(round(abs(float(input("enter a whole positive number : ")))))
