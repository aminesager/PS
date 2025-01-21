class Stack:
    def __init__(self):
        self.stack = []



    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        else:
            raise IndexError("pop from empty stack")

    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
        else:
            raise IndexError("peek from empty stack")

    def size(self):
        return len(self.stack)

# Example usage
stack = Stack()
stack.push(10)
stack.push(20)

stack.push(1)
stack.push(1)
stack.push(15)


print(stack.peek())  # Output: 20
print(stack.size())  # Output: 1