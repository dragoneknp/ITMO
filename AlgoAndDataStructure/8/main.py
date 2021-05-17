def dfs(vertex,c):
    global vizited,color
    q=[vertex]
    vizited[vertex] = 1
    while q:
        x=q.pop()
        color[x]=c
        for i in d[x]:
            if not vizited[i]:
                vizited[i]=1
                q.append(i)


file = open("components.in", "r")
fin = file.readline().split()
n, m = int(fin[0]), int(fin[1])
d = [[] for i in range(n)]
color=[0]*n
vizited = [0] * n

for i in range(m):
    fin = file.readline().split()
    k, p = int(fin[0]), int(fin[1])
    d[k - 1].append(p - 1)
    d[p - 1].append(k - 1)
k=0
for i in range(n):
    if not vizited[i]:
        k+=1
        dfs(i,k)
fout=open("components.out","w")
print(k,file=fout)
print(*color,file=fout)
