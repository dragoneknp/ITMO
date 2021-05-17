def mergesort(array):
    if len(array) == 1:
        return 0
    else:
        middle = len(array) // 2
        leftside = array[:middle]
        rightside = array[middle:]
        i = 0
        j = 0
        k = 0
        track = 0
        inversion = 0
        a = mergesort(leftside)
        b = mergesort(rightside)
        while i < len(leftside) and j < len(rightside):
            if int(leftside[i]) <= int(rightside[j]):
                array[k] = int(leftside[i])
                i += 1
                k += 1
                track += 1
            else:
                array[k] = int(rightside[j])
                j += 1
                k += 1
                inversion = inversion + len(leftside) - track
        while i < len(leftside):
            array[k] = int(leftside[i])
            i += 1
            k += 1
        while j < len(rightside):
            array[k] = int(rightside[j])
            j += 1
            k += 1
        counter = inversion + a + b
        return counter


file = open("inversions.in", "r")
elements = file.readline()
array = file.readline().split()
v = open("inversions.out", "w")
result = mergesort(array)

v.write(str(result))
