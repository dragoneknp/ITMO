class HashTable:
    def __init__(self, size=1000000):
        self.size = size
        self.table = [[] for i in range(self.size)]

    def hash_placer(self, value):
        place = 1
        for char in value:
            place = (place+ord(char))*111
        return place % self.size

    def finddata(self, data):
        indexofdata = self.hash_placer(data)
        for i in range(len(self.table[indexofdata])):
            if self.table[indexofdata][i][0] == data:
                return i
        return None

    def put(self, data):
        checkdata = self.finddata(data[0])
        if checkdata != None:
            self.table[self.hash_placer(data[0])][checkdata][1] = data[1]
        else:
            self.table[self.hash_placer(data[0])].append(data)

    def delete(self, data):
        checkdata = self.finddata(data)
        if checkdata != None:
            self.table[self.hash_placer(data)][checkdata], self.table[self.hash_placer(data)][-1] = \
            self.table[self.hash_placer(data)][-1], self.table[self.hash_placer(data)][checkdata]
            self.table[self.hash_placer(data)].pop()


hash = HashTable()
filein = open("map.in", "r")
fileout = open("map.out", "w")
line = filein.readline().split()
while line:
    if line[0] == "put":
        hash.put(line[1:])
    elif line[0] == "get":
        f = hash.finddata(line[1])
        if f != None:
            print(hash.table[hash.hash_placer(line[1])][f][1], file=fileout)
        else:
            print("none", file=fileout)
    elif line[0] == "delete":
        hash.delete(line[1])
    line = filein.readline().split()