f = open('aplusbb.in')
l = f.read().split()
a=int(l[0])
b=int(l[1])
f.close()
r = open("aplusbb.out","w")
t=a+b**2
r.write(str(t))
r.close()

