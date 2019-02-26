# Given a linked list, check if the the linked list has loop or not.
# Below diagram shows a linked list with a loop.


# mark visited nodes (not their values) as you traverse list
def detect_loop1(self):
    s = set()
    temp = self.head
    while temp:
        if temp in s:  # ecountering same node for 2nd time
            return True
        temp = temp.next
    return False

# Floyd's cycle-finding algorithm: fastest method, traverse with two pointers
# after the slow and fast pointer always meet when there's cycle
# the extra distance fast pointer travels = distance slow pointer travels


def detect_loop2(self):
    slow, fast = self.head, self.head
    while slow and fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False

# Write a function that checks whether a given Linked List contains loop and if loop is present then returns count of nodes in loop.
# ex. loop is present in below linked list and length of loop is 4. If loop is not present, then function should return 0.
# implementation is almost same as detect_loop2


def detect_loop_count(self):
    slow, fast = self.head, self.head
    start = True  # both slow and fast are at start of list

    while slow and fast and fast.next:
        if slow == fast and start == False: # there is a loop, start to count
            count = 1
            slow = slow.next # move slow one node forward
            while slow != fast:
                slow = slow.next
                count += 1
            return count
        slow = slow.next
        fast = fast.next.next
        start = False
    return 0 # no loop
