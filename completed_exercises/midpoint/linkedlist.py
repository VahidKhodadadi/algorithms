class Node:
    def __init__(self, data, next = None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def insertFirst(self, data):
        self.head = Node(data, self.head)

    def size(self):
        counter = 0
        node = self.head
        while node:
            counter+=1
            node = node.next

        return counter

    def getFirst(self):
        return self.head

    def getLast(self):
        if self.head is None:
            return None

        node = self.head
        while node:
            if node.next is None:
                return node
            node = node.next

    def clear(self):
        self.head = None

    def removeFirst(self):
        if self.head is None:
            return

        self.head = self.head.next

    def removeLast(self):
        if self.head is None:
            return

        if self.head.next is None:
            self.head = None
            return

        previous = self.head
        node = self.head.next
        while node.next != None:
            previous = node
            node = node.next
        
        previous.next = None

    def insertLast(self, data):
        last = self.getLast()

        if last:
            last.next = Node(data) 
        else:
            self.head = Node(data)

    def getAt(self, index):
        counter = 0
        node = self.head
        while node:
            if counter == index:
                return node

            counter += 1
            node = node.next
        return None

    def removeAt(self, index):
        if self.head is None:
            return

        if index == 0:
            self.head = self.head.next
            return

        previous = self.getAt(index - 1)
        if previous is None or previous.next is None:
            return
        previous.next = previous.next.next

    def insertAt(self, data, index):
        if self.head is None:
            self.head = Node(data)
            return

        if index == 0:
            self.head = Node(data, self.head)
            return

        previous = self.getAt(index - 1) or self.getLast()
        node = Node(data, previous.next)
        previous.next = node

    def forEach(self, fn):
        node = self.head
        counter = 0
        while node:
            fn(node, counter)
            node = node.next
            counter += 1
