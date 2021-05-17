file= open('check.in', 'r')
fileout = open('check.out', 'w')
n = int(file.readline())
if n:
    d = [0] * n
    array = [[0, 0, 0] for i in range(n)]
    for i in range(n):
        d = file.readline().split()
        value, left, right = int(d[0]), int(d[1]), int(d[2])
        left -= 1
        right -= 1
        array[i][0] = value
        array[i][1] = left
        array[i][2] = right

    flag = 1
    dl = [[0, 10000000000, -10000000000]]
    while dl and flag:
        pars = dl.pop()
        num = pars[0]
        ap = pars[1]
        al = pars[2]
        value, left, right = array[num][0], array[num][1], array[num][2]

        if value >= ap or value <= al:
            flag = 0
            break

        if left != -1:
            if array[left][0] >= array[num][0]:
                flag = 0
                break
            dl.append([left, value, al])
        if right != -1:

            if array[right][0] <= array[num][0]:
                flag = 0
                break
            dl.append([right, ap, value])

    if flag:
        print('YES', file=fileout)
    else:
        print('NO', file=fileout)
else:
    print('YES', file=fileout)
fileout.close()
