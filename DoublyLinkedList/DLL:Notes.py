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

my_doubly_linked_list = DoublyLinkedList(7)
my_doubly_linked_list.print_list()
