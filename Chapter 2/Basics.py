# From Geekforgeeks linkedlist implementation


class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:

    def __init__(self):
        self.head = None

    def findLength(self):
        temp = self.head
        count = 0
        while(temp):
            count += 1
            temp = temp.next
        return count

    def printLst(self):
        temp = self.head
        while(temp):
            print(temp.data)
            temp = temp.next

    def addHead(self, data):
        newHead = Node(data)
        newHead.next = self.head
        self.head = newHead

    def addAfter(self, prevNode, data):
        if prevNode == None:
            return

        newNode = Node(data)
        newNode.next = prevNode.next
        prevNode.next = newNode

    def addTail(self, data):
        newTail = Node(data)
        if self.head == None:
            self.head = newTail
            return

        tail = self.head
        while tail.next:
            tail = tail.next
        tail.next = newTail

    def deleteNode(self, toDelete):
        temp = self.head

        if temp and temp.data == toDelete:
            self.head = temp.next
            temp = None  # unlink node from list
            return

        while temp:
            if temp.data == toDelete:
                break
            prev = temp
            temp = temp.next

        if temp:
            return
        prev.next = temp.next
        temp = None

    def does_exist(self, x):
        temp = self.head
        while temp:
            if temp.data == x:
                return True
            temp = temp.next
        return False

    def get_nth(self, n):
        temp = self.head
        count = 0
        while temp:
            if count == n:
                return temp.data
            count += 1
            temp = temp.next
        assert(False) # nth element doesn't exist
        return 0

lst = LinkedList()
for i in range(10):
    lst.addTail(i)
lst.printLst()


