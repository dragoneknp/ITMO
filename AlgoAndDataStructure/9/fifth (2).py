def dfs(vertex):
    global flag1, color
    q = [(vertex, 1)]
    while q:
        x, color1 = q.pop()
        color[x] = color1
        for i in d[x]:
            if color[i] == 0:
                q.append((i, -color1))
            elif color[i] == color1:
                flag1 = 0
                return


file = open("bipartite.in", "r")
fin = file.readline().split()
n, m = int(fin[0]), int(fin[1])

d = [[] for i in range(n)]
color = [0] * n
flag1 = 1
for i in range(m):
    fin = file.readline().split()
    k, p = int(fin[0]), int(fin[1])
    d[k - 1].append(p - 1)
    d[p - 1].append(k - 1)

for i in range(n):
    if color[i] == 0:
        dfs(i)

fout = open("bipartite.out", "w")
if flag1 == 0:
    print("NO", file=fout)
else:
    print("YES", file=fout)
