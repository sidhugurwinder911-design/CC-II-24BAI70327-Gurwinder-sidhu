from collections import deque

class MyStack:
    def __init__(self):
        self.q = deque()

    def push(self, x):
        self.q.append(x)
        for i in range(len(self.q) - 1):
            self.q.append(self.q.popleft())

    def pop(self):
        return self.q.popleft()

    def top(self):
        return self.q[0]

    def empty(self):
        return len(self.q) == 0


stack = MyStack()

n = int(input("How many elements do you want to push? "))

for i in range(n):
    x = int(input("Enter element: "))
    stack.push(x)

print("Top Element:", stack.top())
print("Popped Element:", stack.pop())

if not stack.empty():
    print("Top After Pop:", stack.top())

print("Is Stack Empty?", stack.empty())