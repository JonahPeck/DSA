#binary tree is essentially a linked list starting with a node that has pointers to the left and right 
#each pointer points to the left or the right 
#in a full tree each node either points to zero nodes or two nodes
#a perfect tree represents a tree that is level all the way across 
#top node pointing to other nodes is known as the parent node pointing to a child node
#nodes with the same parent are known as siblings 
#every node can onlu have one parent
{
    "value": 4,
    "left": None,
    "right" None
}

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

#within a binary search tree, nodes need to be laid out in a certain way
#if the child node is greater in value than the parent node it will go on the right, 
#if it is less than it will go on the left

#binary search tree Big O is O(log n)
#lookup, insery and remove are treated as O(log n)