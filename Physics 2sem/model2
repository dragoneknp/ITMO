import matplotlib.pyplot as plt
import math
U = 220
q = 1.6 * 10 ** -19
m = 9.11 * 10 ** -31
V = 0
R2 = 0.6
R1 = 0.25
Vx = 7.5 * 10 ** 6
Vy = 0
l = 0.14
x = 0
y = (R2 - R1) / 2
h = 1 / 10 ** 12
arrY = []
arrX = []
arrA = []
arrV = []
arrVy = []
i = 0
while x <= l:
    a = (q / m) * (U / (math.log(R2 / R1) * (R1 + y)))
    V = math.sqrt(Vx**2 + Vy**2)
    Vy = Vy + a * h
    y = y + Vy * h
    x = x + Vx * h
    arrA.append(a)
    arrV.append(V)
    arrY.append(y)
    arrX.append(x)
    arrVy.append(Vy)

    i += 1

iter = 0
a = 0
while iter < 5000:
    y = y + Vy * h
    x = x + Vx * h
    arrY.append(y)
    arrX.append(x)
    arrA.append(0)
    arrVy.append(Vy)
    arrV.append(V)
    iter += 1
    i += 1

tg = [_ for _ in range(i)]

plt.plot(arrY, arrX)
plt.xlabel("x")
plt.ylabel("y")
plt.show()

plt.plot(tg, arrY)
plt.xlabel("t")
plt.ylabel("y(t)")
plt.show()

plt.plot(tg, arrV)
plt.xlabel("t")
plt.ylabel("V(t)")
plt.show()

plt.plot(tg, arrA)
plt.xlabel("t")
plt.ylabel("a(t)")
plt.show()

plt.plot(tg, arrX)
plt.xlabel("t")
plt.ylabel("x(t)")
plt.show()
