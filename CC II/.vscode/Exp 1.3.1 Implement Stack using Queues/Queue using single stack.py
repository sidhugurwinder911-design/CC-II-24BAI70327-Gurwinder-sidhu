class MyQueue:
    def __init__(self):
        self.stack = []

    def push(self, x):
        self.stack.append(x)
        print(f"Enqueued: {x}")

    def pop(self):
        if not self.stack:
            print("Queue is Empty")
            return

        if len(self.stack) == 1:
            x = self.stack.pop()
            print(f"Dequeued: {x}")
            return x

        temp = self.stack.pop()
        item = self.pop()
        self.stack.append(temp)
        return item

    def front(self):
        if not self.stack:
            print("Queue is Empty")
            return

        if len(self.stack) == 1:
            print(f"Front Element: {self.stack[-1]}")
            return self.stack[-1]

        temp = self.stack.pop()
        item = self.front()
        self.stack.append(temp)
        return item

    def empty(self):
        return len(self.stack) == 0


# -------- Driver Code --------
queue = MyQueue()

queue.push(10)
queue.push(20)
queue.push(30)
queue.push(40)

print("\nCurrent Stack:", queue.stack)

queue.front()

queue.pop()
print("After Dequeue:", queue.stack)

queue.front()

queue.pop()
print("After Dequeue:", queue.stack)

queue.pop()
print("After Dequeue:", queue.stack)

queue.pop()
print("After Dequeue:", queue.stack)

print("\nIs Queue Empty?", queue.empty())