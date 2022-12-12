from tkinter import END
from turtle import end_fill


r = int(input("how many rows?:"))
c = int(input("how many columns?: "))
symbol = input("enter any symbols")
for i in range(r):
    for j in range(c):
        print(symbol, end="")
    print()
