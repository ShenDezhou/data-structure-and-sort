class Node:
    def __init__(self, value):
        self.data = value
        self.pointer = None

class Link:
    def __init__(self, node):
        self.head = node
        self.tail = node

    def add(self, node):
        current = self.head
        while self.head.pointer:
            current = current.pointer
        else:
            current.pointer = node

if __name__ == '__main__':
    root = Node(0)
    l = Link(root)
    l.add(Node(1))
    print(l)