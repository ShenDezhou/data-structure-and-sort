class Heap:
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
            if self.data[p] < self.data[i]:
                self.data[p], self.data[i] = self.data[i], self.data[p]
            else:
                break
            i = p

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
            if self.data[l] > self.data[r]:
                target = l
            else:
                target = r
            if self.data[target] > self.data[current]:
                self.data[target], self.data[current] = self.data[current], self.data[target]
            else:
                break
            current = target
        return root

if __name__ == "__main__":
    h = Heap()
    [h.push(i) for i in range(10)]
    a = h.pop()
    b = h.pop()
    c = h.pop()
    print(a, b, c)
