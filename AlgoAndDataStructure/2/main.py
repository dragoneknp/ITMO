from random import randint


def quicksort(array):
    if len(array) <= 1:
        return array
    else:
        randomelement = int(array[randint(0, len(array)) - 1])
        low = []
        medium = []
        high = []
        for element in array:
            if int(element) > int(randomelement):
                high.append(int(element))
            elif int(element) < int(randomelement):
                low.append(int(element))
            else:
                medium.append(int(element))
        return quicksort(low) + medium + quicksort(high)


f = open("sort.in")
elements = f.readline()
array = f.readline().split()
array = quicksort(array)
array = [str(element) for element in array]
v = open("sort.out", "w")
v.write(" ".join(array))
