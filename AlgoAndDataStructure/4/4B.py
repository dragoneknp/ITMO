class Queue:
    def __init__(self):
        self.queue = []

    def push(self, elem):
        self.queue+=[elem]

    def pop(self):
        self.queue=self.queue[1:]


file = open('queue.in', 'r')
queue = Queue()
n = int(file.readline())
fileout = open('queue.out', 'w')
for i in range(n):
    queuein = file.readline().split()
    sign = queuein[0]
    if sign == "+":
        queue.push(queuein[1])
    else:
        print(queue.queue[0], file=fileout)
        queue.pop()
