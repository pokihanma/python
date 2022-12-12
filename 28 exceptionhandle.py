'''#exception handling = by using this method events during execution that interrupt the flow of a program'''
from logging import exception


try:
    num1 = int(input("enter the number; "))
    num2 = int(input("enter the second number: "))
    num3 = num1/num2
   # print(num3)
#except ZeroDivisionError:
 #   print("it can be divide by zero")    
#except exception:
   # print("its wrong input method") 
#except ValueError:
   # print("enter number only not letters")
except ZeroDivisionError as e:
    print(e)
else:
    print(num3)   
finally:
    print("this will executed") #whether exception accur or not it will run     
    