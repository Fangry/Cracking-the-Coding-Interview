'''
Write code to remove duplicates from an unsorted linked list.
FOLLOW UP
How would you solve this problem if a temporary buffer is not allowed?
'''


def removeDups(lst):
    if lst == None:
        return

    temp = lst.head
    prev = None
    tracker = []

    while temp:
        if temp.data in tracker:
            prev.next = temp.next
        else:
            tracker.append(temp.data)
            prev = temp
        temp = temp.next

