def bfs():
    global flag
    q = []
    for i in range(n):
        if len(d[i]) == 0:
            q.append(i)
            color[i] = -1
    mn = []

    while q:
        x = q.pop()
        for i in d1[x]:
            if color[i] == 0:
                color[i] = -color[x]
                mn.append(i)
            elif color[i] == -1 and color[x] == -1:
                color[i] = 1
                mn.append(i)
        if len(q) == 0:
            q = mn[:]
            mn = []


file = open("game.in", "r")
fin = file.readline().split()
n, m, s = int(fin[0]), int(fin[1]), int(fin[2])
d = [[] for i in range(n)]
d1 = [[] for i in range(n)]
color = [0] * n
flag = 0
for i in range(m):
    fin = file.readline().split()
    a, b = int(fin[0]), int(fin[1])
    d[a - 1].append(b - 1)
    d1[b - 1].append(a - 1)
fout = open("game.out", "w")
bfs()
if color[s - 1] == 1:
    print("First player wins",file=fout)
else:
    print("Second player wins",file=fout)
