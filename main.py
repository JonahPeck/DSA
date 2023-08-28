# # data structures
# lists - list - unorded sequence of objects 
# dict - dict -unordered key value pair
# tuples - tup - ordered imutable sequence of objects 
# Sets - set - unordered collection of unique objects
# Booleans - bool - Logical value indicating True of False


#mod operator (%) returns the remainder of the divided number 


# print("hello my name is {2}".format("Jonah", "maile", "Bob"))
# number = 10000/7362
# print("The number is {n:1.4f}".format(n=number))
# name = "Jon"
# print("Hello " + name)

# Big O notation - comparing code based off of efficiency
# Time complexity is not measured in time it is measured in the number of operations it takes to complete something
# Space complexity is measured based on memory usage
# Greek letters needed to know are Omega, Theta, And Omicron.
# Omega is the best case scenario for running code, Theta is the average and Big O is the worst case

# def print_items(n):
#     for i in range(n):
#         for j in range(n):
#          print(i,j)

#     for k in range(n):
#         print(k)

# print_items(10)

# def add_items(n):
#     return n + n

# add_items(5)

# This is an example of O(n)
# O(n) is proportional on a graph.
# O(2n) is the same as 0(n) - all constants are dropped.

# O(n*n) is much less efficent from a time complexity standpoint

# Drop non-dominants means we must drop whatever the smaller function is when working within time complexity
# O(1) is referred to as constant time meaning that as it increases the number of operations will remain constant.

# different terms for inputs cannot be simplified down. They must remain constant.
# Such as O(a+b) cannot equal O(n)

# Lists - O(n) if the indexing is happening from the front of the list and O(1) if from the back of the list

#every data structure that we are going to create is coming from a class

# constructor syntax
# class Cookie:
# # def __init__(self, color):
# #     self.color = color
# cookie_one = Color('green')

# class Cookie:
#     def __init__(self,color):
#         self.color = color

#     def get_color(self):
#         return self.color

#     def set_color(self,color):
#         self.color = color

# cookie_one = Cookie('green')
# cookie_two = Cookie('blue')

# print("Cookie one is", cookie_one.get_color())
# print("Cookie two is", cookie_two.get_color())


# cookie_one.set_color('yellow')

# print("\nCookie one is now", cookie_one.get_color())
# print("Cookie two is", cookie_two.get_color())

#classes will be used in DS&A

# class LinkedList:
#     def __init__(self,value):
    
#     def append(self, value):
#     def pop(self):
#     def prepend(self, value):
#     def insert(self,index, value):
#     def remove(self, value):
    

#pointers
# num1 = 11
# num2 = num1

# print("Before num2 value is updated:")
# print("num1 = ", num2)
# print("num2 = ", num2)

# print("\nnum1 points to:", id(num1))
# print("num2 points to:", id(num2))

# LinkedList - does not have an index - all of the nodes will be spread all over the place
#variables known as head and tail which point to the first and last items.

# A list can have an index within a data structure because each node is next to each other.
# A LinkedList points to the next node but is not next to it and therefore it cannot have an index. 

# LinkedLists and BigO

# Appending a new node to the end of a linked list - O(1)
# Removing a node from the end of a linked list - O(n) because you had to iterate through the whole list
# Adding a node to the front of a linked list - O(1)
# Removing a node from the front of a linked list - O(1)
# Adding a node to the middle of the linked list - O(n) because you have to iterate through the list
# Removing a node from the middle of the linked list - O(n) because you have to iterate through the list
# Lookup a node through a linked list - O(n)

#A noe is the value as well as the pointer. Essentially a key value pair of "4" and "None"

# head = {
#     "value": 11,
#     "next": {
#         "value": 3,
#         "next": {
#             "value": 23,
#             "next": {
#                 "value": 7,
#                 "next": None
#                 }
#             }
#         }
#     }
# print(head['next']['next']['value'])

# #This will only run with a linked list
# print(my_linked_list.head.next.next.value)

#constructors
# A Constructor will create a new node 

# class Node:
#     def __init__(self, value):
#         self.value = value
#         self.next = None
# class LinkedList:
#     def __init__(self, value):
#         new_node = Node(value)
#         self.head = new_node
#         self.tail = new_node
#         self.length = 1

# my_linked_list = LinkedList(4)
# print(my_linked_list.head.value)

# def print_list(self):
#     temp = self.head
#     while temp is not None:
#         print(temp.value)
#         temp = temp.next

#all this will do is create a constructor
# class Node:
#     def __init__(self, value):

#Appending an Item to the end of a Linked List
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def append(self,value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

        self.length += 1
        return True

my_linked_list = LinkedList(1)
my_linked_list.append(2)
my_linked_list.print_list()

# my_linked_list = LinkedList(4)
# print(my_linked_list)


