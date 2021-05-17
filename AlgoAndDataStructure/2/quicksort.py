

def mergesort(array, p, q, r, ind):
    i=p
    j=r+1
    sortedarray=[]
    sortedindex=[]
    while i<=r and j<=q:

        if( array[i]>array[j]):
            sortedarray.append(array[j])
            sortedindex.append(ind[j])
            j+=1
        else:
            sortedarray.append(array[i])
            sortedindex.append(ind[i])
            i+=1

    while i<=r:

        sortedarray.append(array[i])
        sortedindex.append(ind[i])
        i += 1

    while j<=q:

        sortedarray.append(array[j])
        sortedindex.append(ind[j])
        j += 1

    ind[p:q+1]=sortedindex
    array[p:q + 1]=sortedarray

    return
def DoSort(array, p, q, indexes):
    if(p<q):
        r=(q+p+1)//2
        if((q+p+1)%2==0):
            r=r-1

        DoSort(array, p, r, indexes)
        DoSort(array, r + 1, q, indexes)
        mergesort(array, p, q, r, indexes)
    return

file = open('race.in', 'r')
n = int(file.readline())

country=[]
sportsman=[]
index=[]

for i in range(n):
    read = file.readline().split()
    a=read[0]
    b=read[1]
    sportsman.append(b)
    country.append(a)
    index.append(i)
file.close()
DoSort(country, 0, len(country) - 1, index)
outfile = open('race.out', 'w')
prev=""
for i in range(len(country)):
    if (prev != country[i]):
        prev = country[i]
        print("===", country[i], "===", file=outfile)
        print(sportsman[index[i]], file=outfile)

    else:
        print(sportsman[index[i]], file=outfile)
file.close()
outfile.close()



