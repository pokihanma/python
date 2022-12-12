import re
f = open("python\pokinote.txt",'r')
for line in f:
    res = re.findall(r'\s+@\s+',line)
    if len(res)>0:
        print(res)
f.close()