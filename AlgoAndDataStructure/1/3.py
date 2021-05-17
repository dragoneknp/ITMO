t = open("turtle.in")
r=t.readline().split()
n=int(r[0])
m=int(r[1])
l=[]
b=t.read().split("\n")
for i in range(len(b)):
    l.append(list(b[i].split(" ")))
t.close()





for i in range(n-1,-1,-1):
    for j in range(0,m):
        if i==n-1 and j!=0:
            l[i][j]=int(l[i][j])+int(l[i][j-1])
        elif j==0 and i!=n-1:
            l[i][j]=int(l[i][j])+int(l[i+1][j])
        elif j==0 and i==n-1:
            next
        else:
            l[i][j]=max(int(l[i+1][j]),int(l[i][j-1]))+int(l[i][j])



s=open("turtle.out","w")
s.write(str(l[0][m-1]))
s.close()