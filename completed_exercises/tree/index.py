class Node:
    def __init__(self, data):
        self.data = data
        self.children = []

    def add(self, data):
        self.children.append(Node(data))

    def remove(self, data):
        self.children = [node for node in self.children if node.data != data]

class Tree:
    def __init__(self):
        self.root = None

    def traverseBF(self, fn):
        arr = [self.root]
        while len(arr) > 0:
            node = arr.pop(0)
            arr.extend(node.children)
            fn(node)

    def traverseDF(self, fn):
        arr = [self.root]
        while len(arr) > 0:
            node = arr.pop(0)
            arr = node.children + arr
            fn(node)