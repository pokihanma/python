"""'list = used to store multiple items in a single variable"""
l = ["hello", "hi", "how"]
print(l[0:-1])

print(l[1])

for i in l:
    print(i)

l.append("ice cream")  # adding a element in a list
l.remove("hi")
l.pop()  # removes last element
l.insert(0, "kick")
l.sort()

for i in l:
    print(i)
l.remove()
