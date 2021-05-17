
def main():
    file = open("negcycle.in", "r")
    fin = file.readline()
    n = int(fin)
    INF = 10 ** 9
    distance = [0] * n
    edges = []
    path = [None] * n

    for i in range(n):
        fin = file.readline().split()
        for j in range(n):
            if int(fin[j]) != INF:
                edges.append([i, j, int(fin[j])])
    fout = open("negcycle.out", "w")
    len_edges = len(edges)
    flag = None
    for i in range(n):
        flag = None
        for j in range(len_edges):
            edge0, edge1, edge2 = edges[j]
            if distance[edge1] > distance[edge0] + edge2:
                distance[edge1] = max(-INF, distance[edge0] + edge2)
                path[edge1] = edge0
                flag = edge1
        if flag is None:
            break
    if flag is not None:
        for i in range(n):
            flag = path[flag]
        answer_path = []
        current = flag
        while True:
            answer_path.append(current + 1)
            current = path[current]
            if current == flag:
                answer_path.append(current + 1)
                break
        print("YES", file=fout)
        print(len(answer_path), file=fout)
        print(*answer_path[::-1], file=fout)
    else:
        print("NO", file=fout)


if __name__ == '__main__':
    main()
