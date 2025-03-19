import pandas as pd
import numpy as np
import random
import matplotlib.pyplot as plt

dataset_path='worldcup.csv'
data=pd.read_csv(dataset_path)

np.random.seed(1001)

Time_length = data ["Time"]

num_samples = 10000
sample_size = 40

sample_means= np.array([np.mean(np.random.choice(Time_length,sample_size,replace=True))for _ in range(num_samples)])

mean_sample_means= np.mean(sample_means)

mean_population= np.mean(Time_length)

std_sample_means= np.std(sample_means,ddof=1)

std_population = np.std(Time_length,ddof=1)
std_theoretical = std_population / np.sqrt(sample_size)

print("media de los valores medios en las muestras:",mean_sample_means)
print("media de la población (Time):)",mean_population)
print("Desviacion estandar de los valores medios de las muestras:", std_sample_means)
print("Desviacion estandar teorica (o/sqrt(n)):",std_theoretical)

hist, bins = np.histogram(sample_means,bins=50)

plt.figure(figsize=(10,6))
plt.hist (sample_means, bins=50,edgecolor='1', alpha=1)
plt.title("Histograma de las medidas muestrales")
plt.xlabel("Media de la Muestra")
plt.ylabel("Frecuencia")
plt.legend()
plt.show()