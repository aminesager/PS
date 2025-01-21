class MinStack(object):

    def __init__(self):
        self.stack = []
        self.min_stack = [] 

    def push(self, val):
        self.stack.append(val)
        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)

    def pop(self):
        if not self.is_empty():
            val = self.stack.pop()
            if val == self.min_stack[-1]:
                self.min_stack.pop()
            return val
        else:
            raise IndexError("pop from empty stack")

    def top(self):
        if not self.is_empty():
            return self.stack[-1]
        else:
            raise IndexError("empty stack")

    def getMin(self):
        if not self.is_empty():
            return self.min_stack[-1]
        else:
            raise IndexError("empty stack")

    def is_empty(self):
        return len(self.stack) == 0


min_stack = MinStack()

# Push some values onto the stack
min_stack.push(5)
min_stack.push(3)
min_stack.push(7)
min_stack.push(2)

# Get the current minimum value
print("Current min:", min_stack.getMin())  # Expected output: 2 (since 2 is the smallest value)

# Pop a value and check the top and minimum
print("Popped value:", min_stack.pop())  # Expected output: 2 (last pushed value)
print("Current min after pop:", min_stack.getMin())  # Expected output: 3 (next smallest value)

# Pop another value and check
print("Popped value:", min_stack.pop())  # Expected output: 7
print("Current min after pop:", min_stack.getMin())  # Expected output: 3

# Pop another value and check
print("Popped value:", min_stack.pop())  # Expected output: 3
print("Current min after pop:", min_stack.getMin())  # Expected output: 5

# Finally, pop the last value
print("Popped value:", min_stack.pop())  # Expected output: 5
