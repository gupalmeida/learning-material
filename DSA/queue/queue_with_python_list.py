class Queue:

    def __init__(self):
        self.items = []

    def __str__(self):
        return " ".join([str(e) for e in self.items])

    def is_empty(self):
        return len(self.items) == 0

    def enqueue(self, value):
        self.items.append(value)

    def dequeue(self):
        """ As queue is a FIFO data structure
        the first element must be the one removed
        and than the remaining should have their
        positions shifted.
        To achieve that, the pop method is the
        selected method given it will provide a
        O(n) time + O(1) space.
        A better method like popleft could be
        implemented, as it would provide O(1)
        in both space and time, but let's keep
        this way for now."""
        if self.is_empty():
            return "Queue is empty"
        else:
            return self.items.pop(0)

    def peek(self):
        if self.is_empty():
            return "Queue is empty"
        else:
            return self.items[0]
        

if __name__ == "__main__":
    q = Queue()
    q.enqueue(10)
    q.enqueue(20)
    q.enqueue(30)
    q.enqueue(40)
    print(q)
    dequeued_elements = []
    for _ in range(2):
        dequeued_elements.append( q.dequeue() )
    print(f'Dequeued elements: {" ".join([str(e) for e in dequeued_elements])}')
    print("After dequeueing")
    print(q)
