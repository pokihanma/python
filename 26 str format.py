# str.format() = optional method that gives users
#               more control when displaying output

# number = 1000
import string

animal = "cow"
item = "moon"

# print("the ",animal," jumped over the ",item)
print("the {} jumped over the {}".format("cow", "moon"))
print(" the {} jumped over the {}".format(animal, item))
print(" the {0} jumped over the {1}".format(animal, item))

name = "poki"
print("hello, my name is {}".format(name))
print("hello, my name is {:10} nice to meet u".format(name))
print("hello, my name is {:>10} nice to meet u".format(name))
print("hello, my name is {:^10} nice to meet u".format(name))


number = 3.14259
print("the number of pi is {:.2f}".format(number))


full_number = 1000
print("the full number is {:,}".format(full_number))  # adding cama in the numbers
print(
    "the full number's binary value is is {:b}".format(full_number)
)  # making binaray values
print("the full number's octal value is is {:o}".format(full_number))
print("the full number's hexa decimal value is is {:X}".format(full_number))
print("the full number's hexa decimal value is is {:x}".format(full_number))
print(
    "the full number's scientific value is is {:E}".format(full_number)
)  # scientific notiation
print("the full number's scientifyic value is is {:e}".format(full_number))


print("%0.1f" % 4.35345)


s = "hello programimg"
print(s.center(30))
print(s.count("m"))
print("SFGG".isalpha())
print(s.upper())
print(s.isalpha())
