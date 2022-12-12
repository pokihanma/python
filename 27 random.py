import random

x = random.randint(1, 6)
print(x)
y = random.random()
print(y)
mylist = ["rock", "paper", "scissors"]
z = random.choice(mylist)# it will choose any random number in the given range 
print(z)

cards = [1, 2, 3, 4, 5, 6, 7, 8, 9, "J", "K", "Q", "A"]
random.shuffle(cards)#it wil suffle the cards in the list
print(cards)
