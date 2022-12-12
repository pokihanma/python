class Node:
   def __init__(self, data):
       
       self.data = data
       self.next = None

class Queue_structure:
   def __init__(self):
      self.head = None
      self.last = None

   def enqueue_operation(self, data):
      if self.last is None:
         self.head = Node(data)
         self.last = self.head
      else:
         self.last.next = Node(data)
         self.last = self.last.next

   def dequeue_operation(self):
      if self.head is None:
         return None
      else:
         val_returned = self.head.data
         self.head = self.head.next
         return val_returned

my_instance = Queue_structure()
while True:
    
    print('1.enqueue')
    print('2.dequeue')
    print('3.quit')
    operation = int(input("enter the operation to be performed : "))
    if operation == 1:
        x =int(input("enter the number to enqueue : "))
        my_instance.enqueue_operation(x)
    elif operation == 2:
        
        dequeued = my_instance.dequeue_operation()
        if dequeued is None:
            print('The queue is empty.')
        else:
            print('The deleted element is : ', int(dequeued))
    elif operation == 3:
       break