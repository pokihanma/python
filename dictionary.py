# dictionary = A changeable , unordered colletion of unique key : value
#             pairs fast because they use hashing,allow us to acess a vale quickly
# like set


captials = {"usa": "newyork", "india": "delhi", "china": "beijing", "russia": "moscow"}

print(captials["china"])
# print(captials['germany'])
print(
    captials.get("germany")
)  # check the values is present or not without error even if the values is not present in the dictionary it wont give any errors
print(captials.keys())
print(captials.values())
print(captials.items())  # print all in the dictionary
captials.update({"germany": "berlin"})

for i in captials.items():
    print(i)

captials.update({"usa": "LA"})
captials.pop("china")
captials.clear()
