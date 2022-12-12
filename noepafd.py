# if __name__ == '__main__':
#     l=[]
#     hy={}
#     for _ in range(int(input())):
#         name = input()
#         score = float(input())
#         for key,value in zip(name,score):
#             hy[key]=value
#         l.append(score)
#     l.sort()
#     a=l[0]
#     b=l[1]
    
#     if hy[value]==a:
#         print(hy[key])


# a =int (input())
# b=int(input())
# l=[]
# k=1
# for i in range(a):
#     m=[]
#     for(j) in range(b):
#         if k==j:
#             m.append(1)
#         else:
#             m.append(0)
#     k+=1
#     l.append(m)
# print(l)                
if __name__ == '__main__':
    N = int(input())
    # Lists in Python - Hacker Rank Solution START
    Output = [];
    for i in range(0,N):
        ip = input().split();
        if ip[0] == "print":
            print(Output)
        elif ip[0] == "insert":
            Output.insert(int(ip[1]),int(ip[2]))
        elif ip[0] == "remove":
            Output.remove(int(ip[1]))
        elif ip[0] == "pop":
            Output.pop();
        elif ip[0] == "append":
            Output.append(int(ip[1]))
        elif ip[0] == "sort":
            Output.sort();
        else:
            Output.reverse();      
           