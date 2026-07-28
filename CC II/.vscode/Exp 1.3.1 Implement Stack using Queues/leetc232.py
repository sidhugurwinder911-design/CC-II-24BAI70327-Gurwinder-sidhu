class MyQueue:

    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def push(self, x):
        self.stack1.append(x)

    def pop(self):
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        return self.stack2.pop()

    def peek(self):
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        return self.stack2[-1]

    def empty(self):
        return len(self.stack1) == 0 and len(self.stack2) == 0


# -------- Driver Code --------
queue = MyQueue()

n = int(input("Enter number of elements to push: "))

for i in range(n):
    x = int(input("Enter element: "))
    queue.push(x)

print("\nFront Element (Peek):", queue.peek())
print("Popped Element:", queue.pop())

if not queue.empty():
    print("Front Element after Pop:", queue.peek())

print("Is Queue Empty?", queue.empty())