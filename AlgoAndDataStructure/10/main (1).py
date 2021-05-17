def main():
    def length(x1, x2, y1, y2):
        return (x2 - x1) * (x2 - x1) + (y2 - y1) * (y2 - y1)

    file = open("spantree.in")
    fout = open("spantree.out", "w")
    n = int(file.readline())
    inf = 10 ** 9
    points = [None for _ in range(n)]
    w = [[0] * n for _ in range(n)]

    for i in range(n):
        point_x, point_y = list(map(int, file.readline().split()))
        points[i] = [point_x - 1, point_y - 1]

    for i in range(n):
        x1 = points[i][0]
        y1 = points[i][1]
        for j in range(i):
            x2 = points[j][0]
            y2 = points[j][1]
            w[i][j] = w[j][i] = length(x1, x2, y1, y2)

    dist = [inf] * n
    vizited = [0] * n
    dist[0] = 0
    for i in range(n):
        cur = None

        for j in range(n):
            if not vizited[j] and (cur is None or dist[j] < dist[cur]):
                cur = j

        vizited[cur] = 1
        for j in range(n):
            if not vizited[j] and w[cur][j] < dist[j]:
                dist[j] = w[cur][j]

    print(sum(i ** 0.5 for i in dist), file=fout)


main()
