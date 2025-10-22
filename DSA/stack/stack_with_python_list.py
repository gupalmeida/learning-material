class Stack:
    """Class to generate a Stack using
    Python lists"""

    def __init__(self):
        self.items = []

    def push(self,element):
        """ Push operation to the end of the list
        will be O(1) for both time and space"""
        self.items.append(element)

    def is_empty(self):
        return len(self.items) == 0

    def pop(self):
        if self.is_empty():
            return "Stack has no elements"
        return self.items.pop()

    def clear(self):
        self.items = []

    def __str__(self):
        if self.is_empty():
            return "Stack is empty"
        return "\n".join([str(e) for e in reversed(self.items)])


if __name__ == "__main__":
    my_stack = Stack()
    my_stack.push(10)
    my_stack.push(20)
    my_stack.push(30)
    print(my_stack)
    my_stack.pop()
    print(my_stack)
