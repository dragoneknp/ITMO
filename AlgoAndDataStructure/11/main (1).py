file = open("pathsg.in", "r")
fin = file.readline().split()
n, m = int(fin[0]), int(fin[1])
A = [[10 ** 9] * n for _ in range(n)]
for i in range(m):
    fin = list(map(int, file.readline().split()))
    A[fin[0] - 1][fin[1] - 1] = fin[2]

for k in range(n):
    for i in range(n):
        for j in range(n):
            if i == j:
                A[i][j] = 0
            else:
                A[i][j] = min(A[i][j], A[i][k] + A[k][j])
fout = open("pathsg.out", "w")
for i in range(n):
    for j in range(n):
        print(A[i][j], end=" ", file=fout)
    print(file=fout)
