'''
lists < trees < graphs (difficulty from low to high)
tree: data data structure composed of nodes
    each tree has a root node (not necessary in graph theory, but a good convention)
    root node has >= 0 child nodes
    child node has >= child nodes, and so on 

    can't contain cycles
    can have any data type as values
    can have links back to their parent nodes
'''

# simplest implementation for generic tree
class Node:
    def __init__(self, data):
        self.data = data.self
        self.children = []


class Tree:
    def __init__(self):
        self.root = None

