# class ig{
#     // 5  
#     //less<= >= greater taget
#     //1 2 5 8 7 44
#     //3 4
#     //else not allowed 
#     static void (int a[],int target){

#
# }

a = int(input())
m=0
b = [3,3,3]
x =len(b)
for i in range(x):
    
    if b[i]<=a:
        m=m+1
y = x-m
b = set(b)
b = list(b)
if  len(b) ==1 and b[0]==x and a==x:
    y=x   

print(m)
print(y)