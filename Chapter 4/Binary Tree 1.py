# Taken from Geeksforgeeks & this book
'''
Binary tree: each node has up to 2 children
Ternary tree: each node has up to 3 children
so on and so forth...

Binary search tree: a special binary tree, every node fits a specific order
    if value < root, add it to left child
    if value > root, add it to right child
    if first level full, repeat progress as you go to higher lvls, putting new values at new spots

Full binary tree: every node has either 0/2 children, or no nodes have only one child
Perfect binary tree: tree has max. nodes for its lvl, all leaf nodes at same lvl. (tree looks like a complete pyramid)   
Degenerate tree: every node has exactly one child, such trees are same as linked list

'''


class Node:
    
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)



