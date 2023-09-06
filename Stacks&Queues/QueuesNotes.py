#opposite of a stack is a queue - First in first out
#adding people to the list is in-queue, de-queue is removing 
#head and tail are reffered to as first and last

#queue constructor 
class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

class Queue:
    def __init__(self, value):
        new_node = Node(value)
        self.first = new_node
        self.last = new_node
        self.length = 1

    def print_queue(self):
        temp = self.first
        while temp:
            print(temp.value)
            temp = temp.next
    #enqueue or adding to a queue
    def enqueue(self,value):
        new_node = Node(value)
        if self.first is None:
            self.first = new_node
            self.last = new_node
        else:
            self.last.next = new_node
            self.last = new_node
        self.length += 1 
    
    def dequeue(self):
        if self.length == 0:
            return None
        temp = self.first
        if self.length == 1:
            self.first = None
            self.last = None
        if self.length > 1:
            self.first = self.first.next
            temp.next = None
        self.length -= 1
        return temp



my_queue = Queue(4)
my_queue.enqueue(5)
my_queue.enqueue(6)
my_queue.enqueue(7)
my_queue.dequeue()

my_queue.print_queue()
