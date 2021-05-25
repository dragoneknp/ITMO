import math
import matplotlib.pyplot as plt
 
teta, Mr, Mt, u, alpha = map(int, input().split())
Mearth = 5.972e+24
teta = 90 - teta
# 80 30 40 250 20
R = 6371 * 10 ** 3
g0 = 6.67e-11 * Mearth / R / R
 
x, y = 0, 1
v = 0
i = 0
h = 0.1
m = Mt + Mr
Vx = 0
Vy = 0
plot_m, plot_v, plot_x, plot_y = [], [], [], []
plot_Vx, plot_Vy = [], []
i = 0
 
while y >= 0:
    g = g0 * R * R / ((R + y) * (R + y))
 
    if m - Mr > 0:
        Vx += math.sin(teta * math.pi / 180) * u * alpha * h / (m - alpha * h)
        Vy += math.cos(teta * math.pi / 180) * u * alpha * h / (m - alpha * h)
        m -= alpha * h
    Vy -= g * h
 
 
    if Vx != 0:
        teta = math.atan2(Vy, -Vx) * 180 / math.pi - 90

    else:
        if Vy >= 0:
            teta = 0
        else:
            teta = 180
 
    x += Vx * h
    y += Vy * h
 
    plot_m.append(m - Mr)
    plot_v.append(math.sqrt(Vx ** 2 + Vy ** 2))
    plot_x.append(x)
    plot_y.append(y)
    plot_Vx.append(Vx)
    plot_Vy.append(Vy)
    i += 1
 
tg = [_ for _ in range(i)]
 

plt.plot(tg, plot_m)
plt.xlabel("t")
plt.ylabel("m(t)")
plt.show()
 
plt.plot(plot_x, plot_y)
plt.xlabel("x")
plt.ylabel("y")
plt.show()
 

plt.plot(tg, plot_v)
plt.xlabel("t")
plt.ylabel("V(t)")
plt.show()
 
plt.plot(tg, plot_Vy)
plt.xlabel("t")
plt.ylabel("Vy")
plt.show()
 
plt.plot(tg, plot_Vx)
plt.xlabel("t")
plt.ylabel("Vx")
plt.show()
