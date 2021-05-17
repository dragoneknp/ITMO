def dfs(vertex):
    global flag1, color, answer
    q = [vertex]
    while q:
        x = q[-1]
        break_point = 1
        for i in d[x]:
            if color[i] == 0:
                color[i] = 1
                break_point = 0
                q.append(i)
                break
            elif color[i] == 1:
                flag1 = 0
                color[i] = -1
                break_point = 0
                answer.append(i + 1)
                q.append(i)
                break
        if break_point:
            if flag1 == 0:
                return
            q.pop()
            color[x] = -1


file = open("cycle.in", "r")
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
    if color[i] == 0 and flag1 == 1:
        color[i] = 1
        dfs(i)

fout = open("cycle.out", "w")
if flag1 == 0:
    print("YES", file=fout)
    print(*answer, file=fout)
else:
    print("NO", file=fout)
