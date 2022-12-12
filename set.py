'''set = colloecttion which is ordered,unindexed,no dublicate values'''



things= {"fork","spoon","knife","knife"}
dishes = {"bowl","plate","cup","knife"}

for c in things:
    print(c)
 
things.add("book")
#things.remove("fork")
#things.clear()

#things.update(dishes)    

for i in things:
    print(i)
    
 #dinner = things.union(dishes)
print(things.difference(dishes))    
print(things.intersection(dishes))
