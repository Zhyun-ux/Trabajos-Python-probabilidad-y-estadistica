import pandas as pd
import numpy as np
import random

dataset_path='iris.csv'
data=pd.read_csv(dataset_path)

print("primeras filas del conjunto de datos:")
print(data.head())

conglomerados= data.groupby('Species')

grupos_seleccionados = random.sample(list(conglomerados.groups.keys()),2)

muestra_conglomerado= pd.concat([conglomerados.get_group(grupo)for grupo in grupos_seleccionados])

print("\nMuestreo Conglomeraro (2 grupos seleccionados)")
print(muestra_conglomerado)

especies_seleccionadas= random.sample(data['Species'].unique().tolist(),2),

muestra_polietapica=pd.concat([data[data['Species']== especie].sample(n=3,random_state=42)for especie in especies_seleccionadas])

print("\nMuestreo Polietápico (3 filas de 2 especies seleccionadas):")
print(muestra_polietapica)