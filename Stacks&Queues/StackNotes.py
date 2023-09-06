#can of tennis balls analogy - you can only access the last item that was pushed onto the stack
#lifo - last in first out

#stacks can be unstood through going through web pages and going back to visited pages
#lists can be used - O(n) must add and remove from the end - pop and add
#with a stack with have top and bottom instead of head and tail. Bottom really isn't needed much because
#we only remove and add from the top

#stack constructor - identical to linkedlist nodes
class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

#stack class constructor
class Stack:
    def __init__(self, value):
        new_node = Node(value)
        self.top = new_node
        self.height = 1
    
    def print_stack(self):
        temp = self.top
        #or while temp is not None:
        while temp:
            print(temp.value)
            temp = temp.next
    
    def prepend(self,value):
        new_node = Node(value)
        if self.length == 0:
            return new_node
        else:
            new_node = self.top
            top = self.temp
            self.temp = temp.next
        return temp

my_stack = Stack(4)
my_stack.print_stack()