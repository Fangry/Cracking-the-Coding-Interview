# Binary tree insertion in level order
# Given a binary tree & a key, insert key into binary tree at 1st position available in level order
# tutorialpoint


class Node:

    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

    def insert(self, data):
        if self.val:
            if data <= self.val:  # compare new value with parent node
                if self.left == None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.val:
                if self.right == None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.val = data


def print_in_order(root):
    if root:
        print_in_order(root.left)
        print(root.val)
        print_in_order(root.right)


root = Node(1)
root.left = Node(2)
root.right = Node(3)
print_in_order(root)
print()

root.insert(5)
print_in_order(root)
