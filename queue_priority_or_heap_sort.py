from data_structure.queue_priority import PriorityQueue

if __name__ == "__main__":
    pq = PriorityQueue()
    from data_structure.link import Node
    [pq.push(Node(i)) for i in range(10)]
    b = [pq.pop().data for i in range(10)]
    print(b)
