import pandas as pd
import numpy as np
import random

dataset_path='Titanic-Dataset.csv'
data=pd.read_csv(dataset_path)

np.random.seed(1001)

survive_length = data ["Survived"]

num_samples = 10000
sample_size = 40

sample_means= np.array([np.mean(np.random.choice(survive_length,sample_size,replace=True))for _ in range(num_samples)])

mean_sample_means= np.mean(sample_means)

mean_population= np.mean(survive_length)

std_sample_means= np.std(sample_means,ddof=1)

std_population = np.std(survive_length,ddof=1)
std_theoretical = std_population / np.sqrt(sample_size)

print("media de los valores medios en las muestras:",mean_sample_means)
print("media de la población (Survived.Length):)",mean_population)
print("Desviacion estandar de los valores medios de las muestras:", std_sample_means)
print("Desviacion estandar teorica (o/sqrt(n)):",std_theoretical)