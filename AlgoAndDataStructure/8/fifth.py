def bfs(s):
    global level
    level[s] = 0
    queue = [s]
    while queue:
        v = queue.pop(0)
        for w in d[v]:
            if level[w] == -1:
                queue.append(w)
                level[w] = level[v] + 1
file=open("pathbge1.in","r")
fin=file.readline().split()
n,m=int(fin[0]),int(fin[1])
d = [[] for i in range(n)]
for i in range(m):
    fin = file.readline().split()
    k, p = int(fin[0]), int(fin[1])
    d[k - 1].append(p - 1)
    d[p - 1].append(k - 1)

level = [-1] * len(d)
bfs(0)
fout=open("pathbge1.out","w")
print(*level,file=fout)