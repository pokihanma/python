l = []
number = str(input())
a=len(number)
b=a-4
for i in range(0,a):
    l.append("*")
for i in range(b,a):
    l.append(number[i])  
    
# for i in range(a):
#     print a[i] 
for i in l:
     print(i,end="")
     
    