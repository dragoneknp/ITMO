def heapify(array, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    func = int
    if left < n and func(array[i]) < func(array[left]):
        largest = left

    if right < n and func(array[largest]) < func(array[right]):
        largest = right

    if largest != i:
        array[i] = func(array[i])
        array[largest] = func(array[largest])
        array[i], array[largest] = array[largest], array[i]
        heapify(array, n, largest)


def heapSort(array):
    n = len(array)


    for i in range(n, -1, -1):
        heapify(array, n, i)


    func = int
    for i in range(n - 1, 0, -1):
        array[i] = func(array[i])
        array[0] = func(array[0])
        array[i], array[0] = array[0], array[i]
        heapify(array, i, 0)


file = open("sort.in", "r")
n = file.readline()
array = file.readline().split()

heapSort(array)

fileout = open("sort.out", "w")
array = [str(elem) for elem in array]
print(" ".join(array), file=fileout)
