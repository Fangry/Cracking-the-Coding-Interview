# From Geekforgeeks linkedlist implementation

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
        

lst = LinkedList()
lst.head = Node(0)

for i in range(1, 10):
    lst.addTail(i)
