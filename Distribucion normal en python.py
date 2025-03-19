import numpy as np

import matplotlib.pyplot as plt

from scipy.stats import norm

z= float(input("Ingrese el valor de Z para calcular P(Z sz): "))

probabilidad= norm.cdf(z)



print("La probabilidad P(Z 5 (2)) es: (probabilidad: 4f)")

x = np.linspace(-4, 4, 1000)

y = norm.pdf(x)



plt.figure(figsize= (8, 5))

plt.plot(x, y)



x_fill= np.linspace(-4, z, 1000)

y_fill= norm.pdf(x_fill)

plt.fill_between(x_fill,y_fill, alpha=-0.5, color="blue", label=-f"P(Z 5 (2)) {probabilidad:.4f}")




plt.axvline(x=z, color="red", linestyle= "dashed")

plt.axvline(y=0, color="black", linesidth=1)


plt.xlabel("2")
plt.ylabel("Densidad de Probabilidad")
plt.title("Distribución Normal Estándar")
plt.legend()
plt.grid()

plt.show()