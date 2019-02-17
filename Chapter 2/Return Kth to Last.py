'''
Implement an algorithm to find the kth to last element of a singly linked list.
ex. k = 3 returns the 3rd to the last node in the linked list
We don't have the length of the linked list
This can be done recursively & non-recursively, the iternative code is longer but more efficient
'''


def print_kth_to_last(lst, k):
    temp = lst.head
    if temp == None:
        return

    i = 0
    while i < k-1:
        if temp.next:
            temp = temp.next
            i += 1
        else:
            print('k is too big, out of bound!')
            break

    while temp:
        print(temp.data)
        temp = temp.next


# count k backwards from the last node, then return that node
def node_kth_from_last(lst, k):
    p1, p2 = lst.head, lst.head
    if p1 == None:
        return

    for i in range(k-1):
        if p1:
            p1 = p1.next
        else:
            print('k is too big, out of bound!')
            break

    while p1 != None:
        p1 = p1.next
        p2 = p2.next
    return p2
