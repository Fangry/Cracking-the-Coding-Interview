#  Implement a function to check if a linked list is a palindrome.
# method 1: reverse the linked list and check if it's same as the original
# method 2: iterative approach, pushing the 1st half of the linked list onto a stack then compare it to the 2nd half
# method 3: recursive approach


class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:

    def __init__(self):
        self.head = None

    def printLst(self):
        temp = self.head
        while(temp):
            print(temp.data)
            temp = temp.next

    def addTail(self, data):
        newTail = Node(data)
        if self.head == None:
            self.head = newTail
            return

        tail = self.head
        while tail.next:
            tail = tail.next
        tail.next = newTail

    def clone_reverse(self):
        temp = self.head
        info = []
        new_lst = LinkedList()

        while temp:
            info.append(temp.data)
            temp = temp.next
        for i in range(len(info)-1, -1, -1):
            new_lst.addTail(info[i])

        return new_lst

    def check_palindrome1(self):
        copy = self.clone_reverse()
        temp1, temp2 = self.head, copy.head
        while temp1:
            if temp1.data != temp2.data:
                return False
            temp1 = temp1.next
            temp2 = temp2.next
        return True

    def check_palindrome2(self):
        fast, slow = self.head, self.head
        stack = []

        while fast != None and fast.next != None:
            stack.append(slow.data)
            slow = slow.next
            fast = fast.next.next

        if fast != None:    # has odd number of nodes, skip middle node
            slow = slow.next

        while slow != None:
            if stack.pop() != slow.data:
                return False
            slow = slow.next
        return True

    

lst = LinkedList()
lst.addTail(0)
lst.addTail(1)
lst.addTail(0)
print(lst.check_palindrome1())
print(lst.check_palindrome2())
