import pandas as pd 
#lectura de archivo
dataset_path = 'Titanic-Dataset.csv'
data = pd.read_csv(dataset_path)
#lectura 5 primeras filas
print("Primeras 5 filas:")
print(data.head())

#lectura 5 ultimas filas
print("\nUltimas  filas")
print(data.tail())

#info general del archivo
print("\nInformación general de cada colunma")
print(data.info())

#descripcion del archivo
print("\nDescripcion de la tabla")
print(data.describe())

#valores nulos
print("\nValores nulos en columnas")
print(data.isnull().sum())

#Seleccionar columna
print(data)