f = open('aplusb.in')
l = f.read().split()
a=int(l[0])
b=int(l[1])
f.close()
r = open("aplusb.out","w")
t=a+b
r.write(str(t))
r.close()

