def main():
    file = open("pathmgep.in", "r")
    fin = file.readline().split()
    n, s, f = int(fin[0]), int(fin[1]) - 1, int(fin[2]) - 1
    W = []
    INF = 10 ** 15
    for i in range(n):
        W.append(list(map(int, file.readline().replace("-1", str(INF)).split())))

    distance = [INF] * n
    distance[s] = 0
    vizited = [False] * n
    fout = open("pathmgep.out", "w")
    for i in range(n):
        min_dist = INF
        for j in range(n):
            if not vizited[j] and distance[j] < min_dist:
                min_dist = distance[j]
                min_vertex = j
        if min_dist == INF:
            break
        vizited[min_vertex] = True
        for j in range(n):
            tmp_dist = distance[min_vertex] + W[min_vertex][j]
            if tmp_dist < distance[j]:
                distance[j] = distance[min_vertex] + W[min_vertex][j]
    if distance[f] == INF:
        print(-1, file=fout)
    else:
        print(distance[f], file=fout)
if __name__ == '__main__':
    main()