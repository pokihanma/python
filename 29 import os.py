from importlib.resources import path
import os

path = "C:\\Users\\poki\\Desktop\\test.txt"

if os.path.exists(path):
    print("the location exist!")
    if os.path.isfile(path):
        print("it is a file")

else:
    print("this location doest exist")
    
    #os importing is used to make checking annd update in a os files 