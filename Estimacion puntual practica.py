import pandas as pd
import numpy as np
import random
import matplotlib.pyplot as plt

dataset_path='iris.csv'
data=pd.read_csv(dataset_path)

np.random.seed(1001)

petal_length = data ["Petal.Length"]

num_samples = 10000
sample_size = 40

sample_means= np.array([np.mean(np.random.choice(petal_length,sample_size,replace=True))for _ in range(num_samples)])

mean_sample_means= np.mean(sample_means)

mean_population= np.mean(petal_length)

std_sample_means= np.std(sample_means,ddof=1)

std_population = np.std(petal_length,ddof=1)
std_theoretical = std_population / np.sqrt(sample_size)

print("media de los valores medios en las muestras:",mean_sample_means)
print("media de la población (petal.Length):)",mean_population)
print("Desviacion estandar de los valores medios de las muestras:", std_sample_means)
print("Desviacion estandar teorica (o/sqrt(n)):",std_theoretical)

hist, bins = np.histogram(sample_means,bins=50)

plt.figure(figsize=(10,6))
plt.hist (sample_means, bins=50,edgecolor='black', alpha=0.7)
plt.title("Histograma de las medidas muestrales")
plt.xlabel("Media de la Muestra")
plt.ylabel("Frecuencia")
plt.legend()
plt.show()