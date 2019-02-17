'''
Implement an algorithm to delete a node in the middle (i.e., any node but
the first and last node, not necessarily the exact middle) of a singly linked list, given only access to
that node.
EXAMPLE
Input: the node c from the linked list a - >b- >c - >d - >e- >f
Result: nothing is returned, but the new linked list looks like a - >b- >d - >e- >f 
'''


def del_mid_node(n):
    if n == None or n.next == None:
        return('cannot delete node!')
    next_node = n.next
    n.data = next_node.data
    n.next = next_node.next
    next_node = None
