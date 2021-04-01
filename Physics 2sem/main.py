from math import log, cos, sin
import matplotlib.pyplot as plt

alpha, M, m, u, teta = map(int, input().split()) # Скорость сгорания топлива,масса ракеты,масса топлива,скорость истечения газов,угол взлета
m_earth = 6 * 10 ** 24
m0 = M + m
G = 6.7 * 10 ** (-11)
R = 6371000
g = G * m_earth / R ** 2
C1 = log(m0)
t = 0
while t < m / alpha:
    t += 1
    mt = m0 - alpha * t
    V = -u * log(m0 - alpha * t) + g * t + u * log(m0)
    Vx = V * cos(teta)
    Vy = V * sin(teta)
    C2 = -m0 * u * log(m0) / alpha
    y = u * (m0 / alpha - t) * log(m0 - alpha * t) + g * t ** 2 / 2 + u * t * (log(m0) + 1) + C2
    x = u * (m0 / alpha - t) * log(m0 - alpha * t) + u * t * (log(m0) + 1) + C2
    print(Vx, Vy)
    print(V)
    print(x, y)
    print(mt)
tg = range(0, t)


def m(t):
    return [(m0 - alpha * i) for i in t]


def v(t):
    return [(-u * log(m0 - alpha * i) + g * i + u * log(m0)) for i in t]


def x(t):
    return ([u * (m0 / alpha - i) * log(m0 - alpha * i) + u * i * (log(m0) + 1) + -m0 * u * log(m0) / alpha for i in t])


def y(t):
    return (
    [u * (m0 / alpha - i) * log(m0 - alpha * i) + g * i ** 2 / 2 + u * i * (log(m0) + 1) + -m0 * u * log(m0) / alpha for
     i in t])

# Строим график m(t)
plt.plot(tg, m(tg))
plt.xlabel("t")
plt.ylabel("m(t)")
plt.show()

# Строим график v(t)
plt.plot(tg, v(tg))
plt.xlabel("t")
plt.ylabel("V(t)")
plt.show()

# Строим график x(t)
plt.plot(tg, x(tg))
plt.xlabel("t")
plt.ylabel("x(t)")
plt.show()

# Строим график y(t)
plt.plot(tg, y(tg))
plt.xlabel("t")
plt.ylabel("y(t)")
plt.show()
