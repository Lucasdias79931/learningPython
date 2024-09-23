import matplotlib.pyplot as plt
import numpy as np

def parabola(a, b, c, x):
  return a * x**2 + b * x + c

a = float(input("Digite o valor de a: "))
b = float(input("Digite o valor de b: "))
c = float(input("Digite o valor de c: "))

x_min = -10
x_max = 10

x = np.linspace(x_min, x_max, 100)
y = parabola(a, b, c, x)

plt.plot(x, y)
plt.xlabel("x")
plt.ylabel("y")
plt.title("Parábola")
plt.show()
