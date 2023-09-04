#Doubly linked list constructor
#arrows that point both ways
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        #doubly linked list adds this next line
        self.prev = None

#         {
#             "value": 7,
#             "next": None,
#             "prev": None
#         }
class DoublyLinkedList:
    def __init__(self, value):
        new_node = Node(value)
        #same as creating a singly linked list
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self):
        temp = self.head 
        while temp:
            print(temp.value)
            temp = temp.next
#appending within a doubly linked list 
    def append(self,value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node 
        else:
            self.tail.next = new_node  
            new_node.prev = self.tail  
            self.tail = new_node
        self.length += 1 
        return True
#removes the last node from the list
    def pop(self):
        if self.length == 0:
            return None
        temp = self.tail
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
            temp.prev = None
        self.length -= 1 
        return temp

        


my_doubly_linked_list = DoublyLinkedList(1)
my_doubly_linked_list.append(2)
my_doubly_linked_list.append(3)
my_doubly_linked_list.append(4)
my_doubly_linked_list.append(5)

my_doubly_linked_list.pop()

my_doubly_linked_list.print_list()
#appending within a doubly linked list 
