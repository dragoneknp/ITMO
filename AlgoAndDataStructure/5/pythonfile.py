file = open('height.in', 'r')
fileout = open('height.out', 'w')

n = int(file.readline())
array = [1 for i in range(n)]
answer = 1
if n:

    for i in range(n - 1):
        d = file.readline().split()
        a, l, r = int(d[0]), int(d[1]), int(d[2])
        if l != 0:
            l -= 1
            array[l] = array[i] + 1
            answer = max(answer, array[l])
        if r != 0:
            r -= 1
            array[r] = array[i] + 1
            answer = max(answer, array[r])
    print(answer, file=fileout)

else:
    print(0, file=fileout)

fileout.close()
