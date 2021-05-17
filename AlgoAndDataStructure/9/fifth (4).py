def dfs(vertex):
    global color, answer
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


file = open("hamiltonian.in", "r")
fin = file.readline().split()
n, m = int(fin[0]), int(fin[1])
d = [[] for i in range(n)]
color = [0] * n
answer = []
for i in range(m):
    fin = file.readline().split()
    k, p = int(fin[0]), int(fin[1])
    d[k - 1].append(p - 1)


for i in range(n):
    if color[i] == 0:
        dfs(i)
flg=True
for i in range(1,len(answer)):
    fl = True
    x=answer[i]
    for j in range(len(d[x])):
        if d[x][j]==answer[i-1]:
            fl=False
    if fl:
        flg=False
        break


fout = open("hamiltonian.out", "w")
if flg==False:
    print("NO",file=fout)
else:
    print("YES",file=fout)

