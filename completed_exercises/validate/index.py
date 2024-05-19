def validate(node, min = None, max = None):
    if (max != None and node.data > max):
        return False

    if (min != None and node.data < min):
        return False

    if (node.left and validate(node.left, min, node.data) == False):
        return False

    if (node.right and validate(node.right, node.data, max) == False):
        return False

    return True

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def insert(self, data):
        if (data < self.data and self.left):
            self.left.insert(data)
        elif (data < self.data):
            self.left = Node(data)
        elif (data > self.data and self.right):
            self.right.insert(data)
        elif (data > self.data):
            self.right = Node(data)