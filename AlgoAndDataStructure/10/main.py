file = open("input.txt","r")
fin = file.readline().split()
n, m = int(fin[0]), int(fin[1])
d = [[] for i in range(n)]
for i in range(m):
    fin = file.readline().split()
    k, p = int(fin[0]), int(fin[1])
    d[k-1].append(p-1)
    d[p-1].append(k-1)
fout = open("output.txt","w")
for i in range(n):
    print(len(d[i]),end=" ",file=fout)

