
f = open("smallsort.in")
r = f.readline()
l = f.readline().split()


for i in range(len(l)-1):
    for j in range(len(l)-i-1):
        if int(l[j])>int(l[j+1]):
            l[i]=int(l[i])
            l[j]=int(l[j])
            l[j+1]=int(l[j+1])
            l[j],l[j+1] = l[j+1],l[j]

l = [str(i) for i in l]
v = open("smallsort.out", "w")
v.write(" ".join(l))