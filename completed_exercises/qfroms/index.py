from stack import Stack

class Queue:
    def __init__(self):
        self.first = Stack()
        self.second = Stack()
    
    def add(self, record):
        self.first.push(record)

    def remove(self):
        while self.first.peek():
            self.second.push(self.first.pop())
        
        record = self.second.pop()

        while self.second.peek():
            self.first.push(self.second.pop())

        return record
  

    def peek(self):
        while (self.first.peek()):
            self.second.push(self.first.pop())
        
        record = self.second.peek()

        while (self.second.peek()):
            self.first.push(self.second.pop())

        return record