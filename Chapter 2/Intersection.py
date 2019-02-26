'''
Given two (singly) linked lists, determine if the two lists intersect. Return the
intersecting node. Note that the intersection is defined based on reference, not value. That is, if the
kth node of the first linked list is the exact same node (by reference) as the jth node of the second
linked list, then they are intersecting. 

* Two intersecting linked lists will always have same last node

1. Run through each linked list to get lengths and tail nodes
2. Compare tail nodes, (by reference, not value) if different, return False immediately
3. set 2 pointers to start of each linked list
4. Advance the longer linked list's pointer by difference in lengths
5. Traverse each linked list until pointers are same
'''

def find_intersect(lst1, lst2):
    pass
