def main():
    def dfs(v):

        visited[v] = 1
        for vert in graph[v]:
            if not visited[vert]:
                dfs(vert)

    fin = open("path.in")
    fout = open("path.out", "w")

    inf = 10 ** 20
    n, m, s = list(map(int, fin.readline().split()))
    distance = [inf] * n
    distance[s - 1] = 0
    edges = []
    path = [None] * n
    graph = [[] for _ in range(n)]

    for i in range(m):
        a, b, cost = list(map(int, fin.readline().split()))
        a -= 1
        b -= 1
        edges.append([a, b, cost])
        graph[a].append(b)
    neg_cycle = []
    for i in range(n + 1):
        flag = None
        neg_cycle = []
        for j in range(m):
            edge0, edge1, edge2 = edges[j]
            if distance[edge0] != inf:
                if distance[edge1] > distance[edge0] + edge2:
                    distance[edge1] = distance[edge0] + edge2
                    path[edge1] = edge0
                    flag = edge1
                    neg_cycle.append(edge1)
        if flag is None:
            break
    visited = [0] * n
    if flag:
        for i in neg_cycle:
            if visited[i] == 0:
                dfs(i)

    for i in range(n):
        if visited[i]:
            distance[i] = '-'

    for elem in distance:
        if elem == inf:
            print('*', file=fout)
        else:
            print(elem, file=fout)

    fout.close()


main()
