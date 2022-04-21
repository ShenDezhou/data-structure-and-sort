class Stack:
    def __init__(self):
        self.data = []

    def push(self, node):
        self.data.append(node)

    def pop(self):
        if self.data:
            val = self.data[-1]
            self.data.remove(val)
            return val
        return None

if __name__ == "__main__":
    s = Stack()
    from link import Node
    s.push(Node(1))
    s.push(Node(2))
    a = s.pop()
    b = s.pop()
    print(a,b)