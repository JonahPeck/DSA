#binary tree is essentially a linked list starting with a node that has pointers to the left and right 
#each pointer points to the left or the right 
#in a full tree each node either points to zero nodes or two nodes
#a perfect tree represents a tree that is level all the way across 
#top node pointing to other nodes is known as the parent node pointing to a child node
#nodes with the same parent are known as siblings 
#every node can onlu have one parent
# {
#     "value": 4,
#     "left": None,
#     "right" None
# }

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
#instead of head, the top node is referred to as the root node (self.root)
        self.root = None

#insert method BST
    def insert(self, value):
        new_node = Node(value)
        if self.root is None:
            self.root = new_node
            return True
        temp = self.root
        while (True):
            if new_node.value == temp.value:
                return False
            if new_node.value < temp.value:
                if temp.left is None:
                    temp.left = new_node
                    return True
                temp = temp.left
            else:
                if temp.right is None:
                    temp.right = new_node
                    return True
                temp = temp.right
    
    def contains(self, value):
        temp = self.root
        while temp is not None:
            if value < temp.value:
                temp = temp.left
            elif value > temp.value:
                temp = temp.right 
            else:
                return True
        return False


my_tree = BinarySearchTree()
my_tree.insert(47)
my_tree.insert(21)
my_tree.insert(76)
my_tree.insert(18)
my_tree.insert(27)
my_tree.insert(52)
my_tree.insert(82)

print(my_tree.contains(27))
print(my_tree.contains(17))
# print(my_tree.root.left.value)
# print(my_tree.root.right.value)





#within a binary search tree, nodes need to be laid out in a certain way
#if the child node is greater in value than the parent node it will go on the right, 
#if it is less than it will go on the left

#binary search tree Big O is O(log n)
#lookup, insery and remove are treated as O(log n)