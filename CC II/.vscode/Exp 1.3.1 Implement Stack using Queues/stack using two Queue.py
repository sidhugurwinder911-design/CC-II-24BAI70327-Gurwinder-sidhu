from collections import deque

class MyStack:
    def __init__(self):
        self.q1 = deque()
        self.q2 = deque()

    def push(self, x):
        self.q2.append(x)

        while self.q1:
            self.q2.append(self.q1.popleft())

        self.q1, self.q2 = self.q2, self.q1
        print(f"Pushed: {x}")

    def pop(self):
        if self.empty():
            print("Stack is Empty")
            return
        print(f"Popped: {self.q1[0]}")
        return self.q1.popleft()

    def top(self):
        if self.empty():
            print("Stack is Empty")
            return
        print(f"Top Element: {self.q1[0]}")
        return self.q1[0]

    def empty(self):
        return len(self.q1) == 0


# -------- Driver Code --------
stack = MyStack()

stack.push(10)
stack.push(20)
stack.push(30)
stack.push(40)

print("\nCurrent Stack:", list(stack.q1))

stack.top()

stack.pop()
print("Stack after Pop:", list(stack.q1))

stack.top()

stack.pop()
print("Stack after Pop:", list(stack.q1))

stack.pop()
print("Stack after Pop:", list(stack.q1))

stack.pop()
print("Stack after Pop:", list(stack.q1))

print("\nIs Stack Empty?", stack.empty())