class Stack:
    def __init__(self):
        self.stack=[]
    def push(self,elem):
        self.stack+=[elem]
    def pop(self):
        return self.stack[-1:]
        self.stack=self.stack[0:-1]



file = open('postfix.in', 'r')
stack = Stack()

fileout = open('postfix.out', 'w')
fl = 0
stackin = file.readline().split()

for elem in stackin:
    if elem == "+":
        b = stack.pop()
        a = stack.pop()
        stack.push(a + b)

    elif elem == "-":
        b = stack.pop()
        a = stack.pop()
        stack.push(a - b)

    elif elem == "*":
        b = stack.pop()
        a = stack.pop()
        stack.push(a * b)

    else:
        stack.push(int(elem))

print(stack.pop(), file=fileout)
