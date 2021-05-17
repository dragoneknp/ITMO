class HashTable:
    def __init__(self, size=1000000):
        self.size = size
        self.table = [[] for i in range(self.size)]

    def hash_placer(self, value):
        place = 1
        for char in value:
            place = (place + ord(char)) * 111
        return place % self.size

    def finddata(self, data):
        indexofdata = self.hash_placer(data)
        for i in range(len(self.table[indexofdata])):
            if self.table[indexofdata][i][0] == data:
                return i
        return None

    def put(self, data):
        checkdata = self.finddata(data[0])
        hs = self.hash_placer(data[0])
        if checkdata != None:
            self.table[hs][checkdata][1] = data[1]
            return self.table[hs][checkdata], 0
        else:
            self.table[hs].append(data)
            return self.table[hs][-1], 1

    def next(self, prev_element, next_element):
        if prev_element != None:
            prev_element[3] = next_element

    def prev(self, next_element, prev_element):
        if next_element != None:
            next_element[2] = prev_element

    def delete(self, data):
        checkdata = self.finddata(data[0])
        self.next(data[2], data[3])
        self.prev(data[3], data[2])

        self.table[self.hash_placer(data[0])][checkdata], self.table[self.hash_placer(data[0])][-1] = \
            self.table[self.hash_placer(data[0])][-1], self.table[self.hash_placer(data[0])][checkdata]
        self.table[self.hash_placer(data[0])].pop()


hash = HashTable()
filein = open("linkedmap.in", "r")
fileout = open("linkedmap.out", "w")
line = filein.readline().split()
prev = None
while line:
    if line[0] == "put":
        elem = [None] * 4
        elem[0] = line[1]
        elem[1] = line[2]
        if prev != None:
            if line[0] != prev[0]:
                elem[2] = prev
        newelem = hash.put(elem)
        if newelem[1] == 1:
            hash.next(prev, newelem[0])
        if newelem[1] == 1:
            prev = newelem[0]
    elif line[0] == "get":
        tmp = hash.finddata(line[1])
        if tmp != None:
            print(hash.table[hash.hash_placer(line[1])][tmp][1], file=fileout)
        else:
            print("none", file=fileout)
    elif line[0] == "prev":

        check = hash.hash_placer(line[1])
        check2 = hash.finddata(line[1])

        if check != None and check2 != None:
            tmp = hash.table[check][check2][2]
            if tmp != None:
                print(tmp[1], file=fileout)
            else:
                print("none", file=fileout)
        else:
            print("none", file=fileout)

    elif line[0] == "next":
        check = hash.hash_placer(line[1])
        check2 = hash.finddata(line[1])
        if check != None and check2 != None:
            tmp = hash.table[check][check2][3]
            if tmp != None:
                print(tmp[1], file=fileout)
            else:
                print("none", file=fileout)
        else:
            print("none", file=fileout)
    else:
        check = hash.hash_placer(line[1])
        check2 = hash.finddata(line[1])
        if check != None and check2 != None:
            if prev == hash.table[check][check2]:
                prev = hash.table[check][check2][2]
            hash.delete(hash.table[check][check2])
    line = filein.readline().split()
