# Taken from Geeksforgeeks
'''
Binary tree traversal: 3 methods: in-order (most common), post-order, pre-order
in-order: left, root, right
pre-order: root, left, right
post-order: left, right, root
'''


class Node:
    
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key


def print_in_order(root):
    if root:
        print_in_order(root.left)
        print(root.val)
        print_in_order(root.right)


def print_pre_order(root):
    if root:
        print(root.val)
        print_pre_order(root.left)
        print_pre_order(root.right)


def print_post_order(root):
    if root:
        print_post_order(root.left)
        print_post_order(root.right)
        print(root.val)


def print_in_order_noRecursion(root):
    current = root
    s = []
    done = 0

    while(not done):
        if current != None:
            s.append(current)
            current = current.left
        else:
            if len(s) > 0:
                current = s.pop()
                print(current.val)
                current = current.right
            else:
                done = 1


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

print_in_order(root)
# print_pre_order(root)
# print_post_order(root)
# print_in_order_noRecursion(root)
