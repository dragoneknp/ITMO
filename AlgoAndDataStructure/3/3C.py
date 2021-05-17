file = open('radixsort.in', 'r')

a = (file.readline().split())
n, length, k = int(a[0]), int(a[1]), int(a[2])
array = []
for i in range(n):
    string = str(*(file.readline().split()))
    array.append(string)

for i in range(length - 1, -1, -1):

    barray = [[] for i in range(97, 123)]

    for x in array:
        figure = x[i]

        barray[ord(figure) - 97].append(x)

    array = []
    for ki in barray:
        for kj in ki:
            array.append(kj)

    k -= 1
    if k == 0:
        break

fileout = open('radixsort.out', 'w')
for z in array:
    print(z, file=fileout)

