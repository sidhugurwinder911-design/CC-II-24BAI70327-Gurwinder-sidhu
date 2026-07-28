class MyQueue:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def push(self, x):
        self.stack1.append(x)
        print(f"Enqueued: {x}")

    def pop(self):
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())

        if not self.stack2:
            print("Queue is Empty")
            return

        x = self.stack2.pop()
        print(f"Dequeued: {x}")
        return x

    def peek(self):
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())

        if not self.stack2:
            print("Queue is Empty")
            return

        print(f"Front Element: {self.stack2[-1]}")
        return self.stack2[-1]

    def empty(self):
        return len(self.stack1) == 0 and len(self.stack2) == 0


# -------- Driver Code --------
queue = MyQueue()

queue.push(10)
queue.push(20)
queue.push(30)
queue.push(40)

print("\nStack1:", queue.stack1)
print("Stack2:", queue.stack2)

queue.peek()

queue.pop()
print("Stack1:", queue.stack1)
print("Stack2:", queue.stack2)

queue.peek()

queue.pop()
print("Stack1:", queue.stack1)
print("Stack2:", queue.stack2)

queue.pop()
print("Stack1:", queue.stack1)
print("Stack2:", queue.stack2)

queue.pop()
print("Stack1:", queue.stack1)
print("Stack2:", queue.stack2)

print("\nIs Queue Empty?", queue.empty())