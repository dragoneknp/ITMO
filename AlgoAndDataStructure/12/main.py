n = int(input())
l = list(map(int, input().split()))
f = [1] * n
prev = [-1] * n
for i in range(n):
    for j in range(i):
        if l[i] > l[j] and f[j] + 1 > f[i]:
            f[i] = f[j] + 1
            prev[i] = j

max_index = f.index(max(f))
path = []
pos = max_index
while pos != -1:
    path.append(l[pos])
    pos = prev[pos]

print(max(f))
print(*path[::-1])
