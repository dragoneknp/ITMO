class HashTable:
    def __init__(self,size=250000):
        self.size=size
        self.table=[[] for i in range(self.size)]
    def hash_placer(self,value):
        return value % self.size
    def exist(self,data):
        return data in self.table[self.hash_placer(data)]
    def put(self,data):
        if not self.exist(data):
            self.table[self.hash_placer(data)].append(data)
    def delete(self,data):
        if self.exist(data):
            self.table[(self.hash_placer(data))].remove(data)
        else:
            return
hash=HashTable()
filein=open("set.in","r")
fileout=open("set.out","w")
line=filein.readline()
while line:
    if line[0]=="i":
        hash.put(int(line[7:]))
    elif line[0]=="e":
        if hash.exist(int(line[7:])):
            print("true",file=fileout)
        else:
            print("false",file=fileout)
    elif line[0]=="d":
        hash.delete(int(line[7:]))
    line=filein.readline()
