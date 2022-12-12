class Node:
    def __init__(self, data):
       self.data = data
       self.next = None
 
class Stack:
    def __init__(self):
        self.head = None
 
    def push(self, data):
        if self.head is None:
            self.head = Node(data)
        else:
            new_node = Node(data)
            new_node.next = self.head
            self.head = new_node
 
    def pop(self):
        if self.head is None:
            return None
            
        else:
            popped = self.head.data
            self.head = self.head.next
            return popped
    def display(self):
        if self.head is None:
            print("stack is empty")
        else:
            temp = self.head 
            while (temp != None): 
                print(temp.data, end = " "),
                temp = temp.next
a_stack = Stack()
while True:
    print()
    print('1.push')
    print('2.pop')
    print('3.display')
    print('4.quit')
    operation = int(input('What would you like to do? '))
    if operation == 1:
        a = int(input("enter the number to be pushed : "))
        a_stack.push(a)
    elif operation == 2:
        popped = a_stack.pop()
        if popped is None:
            print('Stack is empty.')
        else:
            print('Popped value: ', int(popped))
    elif operation == 3:
        a_stack.display()
