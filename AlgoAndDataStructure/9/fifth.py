def dfs(vertex):
    global flag1, color, answer
    q = [vertex]
    while q:
        flag = 1
        x = q[-1]
        color[x] = 1
        for i in d[x]:
            if color[i] == 0:
                q.append(i)
                flag = 0
                break
            elif color[i] == 1:
                flag1 = 0
                break
        if flag == 1:
            q.pop()
            color[x] = -1
            answer.append(x + 1)


file = open("topsort.in", "r")
fin = file.readline().split()
n, m = int(fin[0]), int(fin[1])

d = [[] for i in range(n)]
color = [0] * n
answer = []

for i in range(m):
    fin = file.readline().split()
    k, p = int(fin[0]), int(fin[1])
    d[k - 1].append(p - 1)


flag1 = 1
for i in range(n):
    if color[i] == 0:
        dfs(i)

fout = open("topsort.out", "w")
if flag1 == 0:
    print(-1, file=fout)
else:
    print(*answer[::-1], file=fout)
