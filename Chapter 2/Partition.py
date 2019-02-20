'''
Write code to partition a linked list around a value x, such that all nodes less than x come
before all nodes greater than or equal to x. lf x is contained within the list, the values of x only need
to be after the elements less than x (see below). The partition element x can appear anywhere in the
"right partition"; it does not need to appear between the left and right partitions.
* x is like a pivot point
EXAMPLE
Input: 3 -> 5 -> 8 -> 5 - > 10 -> 2 -> 1 [partition = 5)
Output: 3 -> 1 -> 2 -> 10 -> 5 -> 5 -> 8
'''
from Implementation import Node, LinkedList


# create 2 linked lists, one holds values smaller than x, one holds values grater or equal to x
def partition(lst, x):
    small_head, small_tail = None, None
    big_head, big_tail = None, None

    node = lst.head
    while node:
        if node.data < x:
            if small_head:
                small_tail.next, small_tail = node, node 
            else:
                small_head, small_tail = node, node # fill in first node
        else:
            if big_head:
                big_tail.next, big_tail = node, node
            else:
                big_head, big_tail = node, node # fill in firsrt node
        node = node.next

    small_tail.next = big_head  # connect two linked lists together
    temp = LinkedList()
    temp.head = small_head
    return temp
