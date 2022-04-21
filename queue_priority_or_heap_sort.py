from data_structure.heap_link import HeapLink

class PriorityQueue:
    def __init__(self):
        self.data = HeapLink()

    def push(self, node):
        self.data.push(node)

    def pop(self):
        return self.data.pop()

if __name__ == "__main__":
    pq = PriorityQueue()
    from data_structure.link import Node
    [pq.push(Node(i)) for i in range(10)]
    b = [pq.pop().data for i in range(10)]
    print(b)
