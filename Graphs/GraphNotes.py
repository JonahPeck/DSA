# an adjacency list represents the physical image of a graph
#This is an adjacency list
# {
#     'A':['B','E'],
#     'B':['A','C'],
#     'C':['B','D'],
#     'D':['C','E'],
#     'E':['A','D'],

# }

#big O of a graph - space complexity is much greater within a matrix and much less within a list
#removing within a matrix is O(1) wheras it is in O(|E|) for the list

class Graph:
    def __init__(self):
        self.adj_list = {}
    
    def add_vertex(self, vertex):
        self.adjust_list[vertex] = []
    
#neeed to practice this much more to understand how to implement
#hello again old friend