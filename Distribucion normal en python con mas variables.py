import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

z1 = float(input("Ingrese el valor de Z1: "))
z2 = float(input("Ingrese el valor de Z2 (para P(Z >= Z2) o P(Z1 <= Z <= Z2)): "))

probabilidad_menor_igual = norm.cdf(z1)
probabilidad_mayor_igual = 1 - norm.cdf(z2)
probabilidad_entre = norm.cdf(z2) - norm.cdf(z1)

print(f"La probabilidad P(Z ≤ {z1}) es: {probabilidad_menor_igual:.4f}")
print(f"La probabilidad P(Z ≥ {z2}) es: {probabilidad_mayor_igual:.4f}")
print(f"La probabilidad P({z1} ≤ Z ≤ {z2}) es: {probabilidad_entre:.4f}")

x = np.linspace(-4, 4, 1000)
y = norm.pdf(x)

plt.figure(figsize=(12, 6))

# Gráfico de la distribución normal estándar
plt.plot(x, y, label="Distribución Normal Estándar")

# Área para P(Z <= z1)
x_fill_menor = np.linspace(-4, z1, 1000)
y_fill_menor = norm.pdf(x_fill_menor)
plt.fill_between(x_fill_menor, y_fill_menor, alpha=0.3, color="blue", label=f"P(Z ≤ {z1}) = {probabilidad_menor_igual:.4f}")

# Área para P(Z >= z2)
x_fill_mayor = np.linspace(z2, 4, 1000)
y_fill_mayor = norm.pdf(x_fill_mayor)
plt.fill_between(x_fill_mayor, y_fill_mayor, alpha=0.3, color="green", label=f"P(Z ≥ {z2}) = {probabilidad_mayor_igual:.4f}")

# Área para P(z1 <= Z <= z2)
x_fill_entre = np.linspace(z1, z2, 1000)
y_fill_entre = norm.pdf(x_fill_entre)
plt.fill_between(x_fill_entre, y_fill_entre, alpha=0.3, color="orange", label=f"P({z1} ≤ Z ≤ {z2}) = {probabilidad_entre:.4f}")

# Líneas verticales para z1 y z2
plt.axvline(x=z1, color="blue", linestyle="dashed")
plt.axvline(x=z2, color="green", linestyle="dashed")

plt.axhline(y=0, color="black", linewidth=1)
plt.xlabel("Z")
plt.ylabel("Densidad de Probabilidad")
plt.title("Distribución Normal Estándar con Probabilidades Calculadas")
plt.legend()
plt.grid()
plt.show()