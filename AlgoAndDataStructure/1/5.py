import random

f = open("sortland.in")
r = f.readline()
l = f.readline().split()
s=l

def quicksort(l):
    if len(l) <= 1:
        return l
    else:
        mediana = float(l[random.randint(0, len(l)) - 1])
        low = []
        medium = []
        high = []
        for i in l:
            if float(i) < mediana:
                low.append(float(i))
            elif float(i) > mediana:
                high.append(float(i))
            else:
                medium.append(float(i))
        return quicksort(low) + medium + quicksort(high)


l = quicksort(l)
poor=l[0]
rich=l[-1]
medium=l[int(r)//2]
p=0
r=0
m=0
for i in range(len(s)):
    if float(s[i])==poor:
        p=i+1
    elif float(s[i])==rich:
        r=i+1
    elif float(s[i])==medium:
        m=i+1

b=str(p)+" "+str(m)+" "+str(r)



v = open("sortland.out", "w")
v.write(b)