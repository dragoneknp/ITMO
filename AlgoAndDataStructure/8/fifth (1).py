from queue import Queue

file = open("input.txt", "r")
fin = file.readline().split()
n, m = int(fin[0]), int(fin[1])
d = [[None] * m for i in range(n)]
for i in range(n):
    fin = file.readline()

    for j in range(len(fin)):

        if fin[j] == "#":
            d[i][j] = False
        elif fin[j] == ".":
            d[i][j] = True
        elif fin[j] == "S":
            d[i][j] = True
            st = [i, j]
        elif fin[j] == "T":
            d[i][j] = True
            end = [i, j]

dist = [[None] * m for i in range(n)]
dist[st[0]][st[1]] = 0
where = [[False] * m for i in range(n)]
queue = Queue()
queue.put(st)

fout = open("output.txt", "w")
while not queue.empty():
    curent_i, curent_j = queue.get()

    if curent_j - 1 > -1:
        if d[curent_i][curent_j - 1] and dist[curent_i][curent_j - 1] is None:
            dist[curent_i][curent_j - 1] = dist[curent_i][curent_j] + 1
            where[curent_i][curent_j - 1] = "L"
            queue.put([curent_i, curent_j - 1])
    if curent_j + 1 < m:
        if d[curent_i][curent_j + 1] and dist[curent_i][curent_j + 1] is None:
            dist[curent_i][curent_j + 1] = dist[curent_i][curent_j] + 1
            where[curent_i][curent_j + 1] = "R"
            queue.put([curent_i, curent_j + 1])
    if curent_i - 1 > -1:

        if d[curent_i - 1][curent_j] and dist[curent_i - 1][curent_j] is None:
            dist[curent_i - 1][curent_j] = dist[curent_i][curent_j] + 1
            where[curent_i - 1][curent_j] = "U"
            queue.put([curent_i - 1, curent_j])
    if curent_i + 1 < n:
        if d[curent_i + 1][curent_j] and dist[curent_i + 1][curent_j] is None:
            dist[curent_i + 1][curent_j] = dist[curent_i][curent_j] + 1
            where[curent_i + 1][curent_j] = "D"
            queue.put([curent_i + 1, curent_j])
    if dist[end[0]][end[1]] is not None:
        break

curent_i, curent_j = end[0], end[1]
path=[]
if dist[curent_i][curent_j] == None:
    print(-1, file=fout)
else:
    print(dist[curent_i][curent_j], file=fout)

    for i in range(dist[curent_i][curent_j]):

        if where[curent_i][curent_j] == "L":
            path.append("L")
            curent_j += 1
        elif where[curent_i][curent_j] == "R":
            path.append("R")
            curent_j -= 1
        elif where[curent_i][curent_j] == "U":
            path.append("U")
            curent_i += 1
        elif where[curent_i][curent_j] == "D":
            path.append("D")
            curent_i -= 1
for i in range(len(path)-1,-1,-1):
    print(path[i],end="",file=fout)
