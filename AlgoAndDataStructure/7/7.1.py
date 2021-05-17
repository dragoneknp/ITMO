import sys
sys.setrecursionlimit(10**9)
def AVL(vertex):
    global height
    a, b = list[vertex][1], list[vertex][2]
    if height[vertex]:
        return height[vertex]
    if a == -1 and b == -1:
        height[vertex] = 1
        return 1
    elif a == -1:
        height[vertex] = AVL(b) + 1
        return height[vertex]
    elif b == -1:
        height[vertex] = AVL(a) + 1
        return height[vertex]
    else:
        height[vertex] = max(AVL(a), AVL(b)) + 1
        return height[vertex]


filein = open('balance.in', 'r')
fileout = open('balance.out', 'w')
n = int(filein.readline())
list = []
height = [0] * n
for i in range(n):
    d = filein.readline().split()
    list.append([int(i) - 1 for i in d])

answer = []
for i in range(n - 1, -1, -1):
    a, b, c = list[i]
    left, right = 0, 0
    if b != -1:
        left = AVL(b)
    if c != -1:
        right = AVL(c)
    answer.append(right - left)
for i in range(n - 1, -1, -1):
    print(answer[i], file=fileout)


