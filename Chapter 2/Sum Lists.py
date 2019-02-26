'''
You have two numbers represented by a linked list, where each node contains a single
digit. The digits are stored in reverse order, such that the 1 's digit is at the head of the list. Write a
function that adds the two numbers and returns the sum as a linked list.
EXAMPLE
Input: (7-) 1 -) 6) + (5 -) 9 -) 2).Thatis,617 + 295.
Output: 2 -) 1 -) 9. That is, 912.
FOLLOW UP
Suppose the digits are stored in forward order. Repeat the above problem.
EXAMPLE
Input: (6 -) 1 -) 7) + (2 -) 9 -) 5).Thatis,617 + 295.
Output: 9 -) 1 -) 2. That is, 912. 
'''


def sum_fwd(lst1, lst2):    # forward order sum
    n1, n2 = 0, 0
    temp1, temp2 = lst1.head, lst2.head
    multiplier1, multiplier2 = 1, 1

    while temp1 != None:
        n1 += temp1.data*multiplier1
        multiplier1 *= 10
        temp1 = temp1.next
    while temp2 != None:
        n2 += temp2.data*multiplier2
        temp2 = temp2.next
        multiplier2 *= 10

    return n1+n2


def findLength(lst):
    temp = lst.head
    count = 0
    while(temp):
        count += 1
        temp = temp.next
    return count


def sum_bkw(lst1, lst2):    # backward-rder sum
    n1, n2 = 0, 0
    temp1, temp2 = lst1.head, lst2.head
    multiplier1, multiplier2 = 1, 1

    # find out the digit place of lst head
    while(temp1):
        multiplier1 *= 10
        temp1 = temp1.next
    while(temp2):
        multiplier2 *= 10
        temp2 = temp2.next
    temp1, temp2 = lst1.head, lst2.head

    # same as sum_fwd() but multiplier divide by 10 each time
    while temp1 != None:
        n1 += temp1.data*multiplier1
        multiplier1 /= 10
        temp1 = temp1.next
    while temp2 != None:
        n2 += temp2.data*multiplier2
        temp2 = temp2.next
        multiplier2 /= 10

    return int((n1+n2)/10)
