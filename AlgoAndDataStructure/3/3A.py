file = open("isheap.in", "r")
n = int(file.readline())
array = file.readline().split()
array = array[::-1]
array.append("0")
array = array[::-1]
fl = 1
for i in range(1, n):
    if 2 * i <= n:
        if int(array[i]) <= int(array[2 * i]):
            next
        else:
            fl = 0
    elif 2 * i + 1 <= n:
        if int(array[i]) <= int(array[2 * i + 1]):
            next
        else:
            fl = 0
    if fl == 0:
        break
s = ""
if fl:
    s = "YES"
else:
    s = "NO"
fileout = open("isheap.out", "w")
print(s, file=fileout)
