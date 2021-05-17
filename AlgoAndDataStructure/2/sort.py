file = open("antiqs.in", "r")
n = int(file.readline())
array = [0] * n
for i in range(len(array)):
    array[i] = i + 1
for i in range(2, len(array)):
    array[i], array[i // 2] = array[i // 2], array[i]
v = open("antiqs.out", "w")

array = [str(i) for i in array]
v.write(" ".join(array))
