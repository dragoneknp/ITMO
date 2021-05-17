def dfs_for_comp(vertex, c):
    global vizited, color1
    q = [vertex]
    vizited[vertex] = 1
    while q:
        x = q.pop()
        color1[x] = c
        for i in d1[x]:
            if not vizited[i]:
                vizited[i] = 1
                q.append(i)


def dfs_for_top_sort(vertex):
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
        if flag == 1:
            q.pop()
            answer.append(x)


file = open("cond.in", "r")
fin = file.readline().split()
n, m = int(fin[0]), int(fin[1])
d = [[] for i in range(n)]
d1 = [[] for i in range(n)]
color = [0] * n
color1 = [0] * n
vizited = [0] * n
answer = []
d1 = [[] for i in range(n)]
for i in range(m):
    fin = file.readline().split()
    k, p = int(fin[0]), int(fin[1])
    d[k - 1].append(p - 1)
    d1[p - 1].append(k - 1)

for i in range(n):
    if color[i] == 0:
        dfs_for_top_sort(i)
k = 0
for i in answer[::-1]:
    if not vizited[i]:
        k += 1
        dfs_for_comp(i, k)

fout = open("cond.out", "w")
print(len(set(color1)), file=fout)
print(*color1, file=fout)
