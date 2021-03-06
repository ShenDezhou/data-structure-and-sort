class HeapLink:
    def __init__(self):
        self.data = []

    def parent(self, i):
        return (i - 1) // 2

    def left_child(self, i):
        return i * 2 + 1

    def right_child(self, i):
        return i * 2 + 2

    def push(self, node):
        self.data.append(node)
        i = len(self.data) - 1
        while i > 0:
            p = self.parent(i)
            if self.compare(str(self.data[p].data), str(self.data[i].data)) < 0:
                self.data[p], self.data[i] = self.data[i], self.data[p]
            else:
                break
            i = p

    def compare(self, p, q):
        if p == q:
            return 0
        elif int(p + q) > int(q + p):
            return 1
        else:
            return -1

    def pop(self):
        root = self.data[0]
        last = self.data[-1]
        self.data.remove(last)
        self.data.insert(0, last)
        self.data.remove(root)
        current = 0
        while current < len(self.data) - 1:
            l = self.left_child(current)
            if l >= len(self.data):
                break
            r = self.right_child(current)
            if r >= len(self.data):
                r = l
            if self.compare(str(self.data[l].data), str(self.data[r].data)) > 0:
                target = l
            else:
                target = r
            if self.compare(str(self.data[target].data), str(self.data[current].data)) > 0:
                self.data[target], self.data[current] = self.data[current], self.data[target]
            else:
                break
            current = target
        return root


if __name__ == "__main__":
    from link import Node

    h = HeapLink()
    [h.push(Node(i)) for i in range(11)]
    a = h.pop()
    b = h.pop()
    c = h.pop()
    print(a, b, c)
