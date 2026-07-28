from collections import deque

class MyStack:
    def __init__(self):
        self.q = deque()

    def push(self, x):
        self.q.append(x)

        # Rotate the queue
        for _ in range(len(self.q) - 1):
            self.q.append(self.q.popleft())

        print(f"Pushed: {x}")

    def pop(self):
        if self.empty():
            print("Stack is Empty")
            return
        x = self.q.popleft()
        print(f"Popped: {x}")
        return x

    def top(self):
        if self.empty():
            print("Stack is Empty")
            return
        print(f"Top Element: {self.q[0]}")
        return self.q[0]

    def empty(self):
        return len(self.q) == 0


# -------- Driver Code --------
stack = MyStack()

stack.push(10)
stack.push(20)
stack.push(30)
stack.push(40)

print("\nCurrent Stack:", list(stack.q))

stack.top()

stack.pop()
print("Stack after Pop:", list(stack.q))

stack.top()

stack.pop()
print("Stack after Pop:", list(stack.q))

stack.pop()
print("Stack after Pop:", list(stack.q))

stack.pop()
print("Stack after Pop:", list(stack.q))

print("\nIs Stack Empty?", stack.empty())