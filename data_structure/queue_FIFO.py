class FIFOQueue:
    def __init__(self):
        self.__data = []

    def push(self, node):
        self.__data.append(node)

    def pop(self):
        if self.__data:
            value = self.__data[0]
            self.__data.remove(value)
            return value
        return None

from link import Node
q = FIFOQueue()
q.push(Node(0))
q.push(Node(100))
a = q.pop()
b = q.pop()
c = q.pop()
print(a,b,c)
