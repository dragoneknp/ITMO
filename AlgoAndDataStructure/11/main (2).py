from heapq import heappush, heappop


def main():
    file = open("pathbgep.in", "r")
    fin = file.readline().split()
    n, m = int(fin[0]), int(fin[1])
    W = [dict() for i in range(n)]
    for i in range(m):
        fin = file.readline().split()
        a, b, cost = int(fin[0]) - 1, int(fin[1]) - 1, int(fin[2])
        W[a][b] = W[b][a] = cost
    
    distance = [None] * n
    q = []
    q.append((0, 0))
    while q:
        path_len, v = heappop(q)
        if distance[v] is None:
            distance[v] = path_len
            for vertex in W[v]:

                edge_len = W[v][vertex]
                if distance[vertex] is None:
                    heappush(q, (path_len + edge_len, vertex))
    fout = open("pathbgep.out", "w")
    print(' '.join(str(dist) for dist in distance), file=fout)


if __name__ == '__main__':
    main()
