# class Node:
#       def __init__(self, data = None, next=None):
#           self.data = data
#           self.next = next
# class LinkedList:
#   def __init__(self):  
#     self.head = None
 
#   def insert(self, data):
#     newNode = Node(data)
#     if(self.head):
#       current = self.head
#       while(current.next):
#         current = current.next
#       current.next = newNode
#     else:
#       self.head = newNode
#   def printLL(self):
#     current = self.head
#     while(current):
#       print(current.data)
#       current = current.next
#   def insertAtMid(self, x):
#     if(head == None): #if the list is empty
#         head = Node(x)
#     else:
#         newNode = Node(x)
#         ptr = head
#         length = 0
        
#         while(ptr != None):
#             ptr = ptr.next
#             length += 1
#         if(length % 2 == 0):
#             count = length / 2 
#         else:
#             (length + 1) / 2
  
#         ptr = head
#         while(count > 1):
#             count -= 1
#             ptr = ptr.next
#         newNode.next = ptr.next
#         ptr.next = newNode
# l = LinkedList()
# while True :
   
#     print("""1.insert
# 2.print
# 3.insert in middle""")
#     choice = int(input("enter the choice : "))
#     if choice == 1:
#         a =input("enter the number : ")
#         l.insert(a)
#     elif choice ==2:
#         l.printLL()
#     elif choice ==3:
#         x = int(input("enter the number : "))
#         l.insertAtMid(x)
#     else:
#         break

        
# class Node :
#     def __init__(self, d):
#         self.data = d 
#         self.next = None
          
# class LinkedList: 
#     def __init__(self):
#         self.head = None
      
   
#     def push(self, new_data): 
#         new_node = Node(new_data) 
#         new_node.next = self.head 
#         self.head = new_node 
          
#     def insertAtMid(self, x):
       
#         if (self.head == None): 
#             self.head = Node(x) 
  
#         else: 
         
#             newNode = Node(x) 
#             slow = self.head
#             fast = self.head.next
  
#             while (fast != None and 
#                    fast.next != None): 
            
#                 slow = slow.next
  
#                 fast = fast.next.next

#             newNode.next = slow.next
#             slow.next = newNode
  
#     # function to display the linked list 
#     def display(self):
#         temp = self.head 
#         while (temp != None): 
#             print(temp.data, end = " "),
#             temp = temp.next 
# ll = LinkedList()
# ll.push(5)
# ll.push(4)
# ll.push(2)
# ll.push(1)
# print("Linked list before insertion: "),
# ll.display()  
# x = 3
# ll.insertAtMid(x) 
# print("\nLinked list after insertion: "),
# ll.display()

