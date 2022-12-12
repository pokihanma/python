a = "hello world racecar madam"
b = a[::-1]
x = a.split()
y = b.split()
m = len(x)-1
l = []
for i in range(len(x)):
    if x[i]==y[m]:
        l.append(x[i])
    m=m-1
print(max(l))