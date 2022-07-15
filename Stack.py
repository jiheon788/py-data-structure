from collections import deque
from turtle import st
# LIFO
stack = deque()

stack.append(5)
stack.append(4)
stack.append(3)
stack.append(2)
stack.append(1)

print(stack)

stack.pop()
stack.pop()
stack.pop()

print(stack)
