from collections import Counter

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyLinkedList:
    """A simple implementation of a singly linked list with basic operations.
    """
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def delete_with_value(self, data):
        if not self.head:
            return
        if self.head.data == data:
            self.head = self.head.next
            return
        current = self.head
        while current.next:
            if current.next.data == data:
                current.next = current.next.next
                return
            current = current.next

    def find(self, data):
        current = self.head
        while current:
            if current.data == data:
                return True
            current = current.next
        return False
    
    def count_occurrences(self):
        count = Counter()
        elements = []
        current = self.head
        while current:
            elements.append(current.data)
            current = current.next
        count.update(elements)
        return count

    def __str__(self):
        elements = ""
        current = self.head
        while current:
            elements += f"{current.data} "
            current = current.next
        return "[" + elements.strip().replace(" ", ", ") + "]"
    
    def __len__(self):
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        return count
    
if __name__ == "__main__":
    sll = SinglyLinkedList()
    sll.append(1)
    sll.append(2)
    sll.prepend(0)
    sll.append(2)
    sll.append(3)
    sll.prepend(4)
    print( f"Number of elements in the singly linked list: {len(sll)}" ) # output: 3
    print( sll ) # output: [0, 1, 2]
    print( sll.count_occurrences() )