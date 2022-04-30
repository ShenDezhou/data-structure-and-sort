from queue_priority import PriorityQueue

if __name__ == "__main__":
    pq = PriorityQueue()
    from link import Node
    [pq.push(Node(i)) for i in range(11)]
    b = [pq.pop().data for i in range(11)]
    print(b)
