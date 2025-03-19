import pandas as pd

# Cargar los datos del archivo CSV
dataset_path = 'Titanic-Dataset.csv'
data = pd.read_csv(dataset_path)

# Exploración inicial
print("Primeras 5 filas:")
print(data.head())

print("\nÚltimas 5 filas:")
print(data.tail())

print("\nInformación general de cada columna:")
print(data.info())

print("\nDescripción de la tabla:")
print(data.describe())

print("\nValores nulos en columnas:")
print(data.isnull().sum())

# Mostrar las primeras 10 filas
print("\nPrimeras 10 filas del dataset completo:")
print(data.head(10))

# Seleccionar las columnas Name, Age, Sex y Survived y guardarlas en un nuevo DataFrame
selected_data = data[['Name', 'Age', 'Sex', 'Survived']]

# Mostrar las primeras 5 filas del nuevo DataFrame
print("\nPrimeras 5 filas del nuevo DataFrame (selected_data):")
print(selected_data.head())

# Pasajeros que viajaban en primera clase
first_class_passengers = data[data['Pclass'] == 1]
print("\nPasajeros que viajaban en primera clase:")
print(first_class_passengers)

# Pasajeros que sobrevivieron y tienen menos de 18 años
survived_under_18 = data[(data['Survived'] == 1) & (data['Age'] < 18)]
print("\nPasajeros que sobrevivieron y tienen menos de 18 años:")
print(survived_under_18)

# Pasajeros mujeres mayores de 50 años
women_over_50 = data[(data['Sex'] == 'female') & (data['Age'] > 50)]
print("\nPasajeros mujeres mayores de 50 años:")
print(women_over_50)

# Pasajeros que viajaban en tercera clase, no sobrevivieron, y tienen más de 30 años
third_class_not_survived_over_30 = data[(data['Pclass'] == 3) & (data['Survived'] == 0) & (data['Age'] > 30)]
print("\nPasajeros que viajaban en tercera clase, no sobrevivieron, y tienen más de 30 años:")
print(third_class_not_survived_over_30)

# Cantidad de pasajeros que viajaban en primera clase
num_first_class_passengers = len(first_class_passengers)
print(f"\nNúmero de pasajeros que viajaban en primera clase: {num_first_class_passengers}")

# Cantidad de pasajeros menores de 18 años que sobrevivieron
num_survived_under_18 = len(survived_under_18)
print(f"Número de pasajeros menores de 18 años que sobrevivieron: {num_survived_under_18}")

# Cantidad de mujeres mayores de 50 años en el barco
num_women_over_50 = len(women_over_50)
print(f"Número de mujeres mayores de 50 años en el barco: {num_women_over_50}")

# Cantidad de pasajeros que viajaban en tercera clase, no sobrevivieron, y tenían más de 30 años
num_third_class_not_survived_over_30 = len(third_class_not_survived_over_30)
print(f"Número de pasajeros en tercera clase, no sobrevivieron, y tenían más de 30 años: {num_third_class_not_survived_over_30}")

# mostrar las ultimas 10 filas del dataset
print("\nÚltimas 10 filas:")
print(data.tail(10))

#Seleccionar unicamente las columnas Pclass, Fare, Age y survived y guardalas en un nuevo dataframe llamado fare_data
fare_data = data[['Pclass', 'Fare', 'Age', 'Survived']]

#Calcula el precio promedio del boleto (Fare) para los pasajeros que sobrevivieron y no sobrevivieron.
promedio_fare_Survive = data[data['Survived'] == 1]['Fare'].mean()
print(f"\n precio promedio del  del boleto para los pasajeros que sobrevivieron ")
print(promedio_fare_Survive)

promedio_fare_not_survive = data[data['Survived'] == 0]['Fare'].mean()
print(f"\n precio promedio del  del boleto para los pasajeros que no sobrevivieron")
print(promedio_fare_not_survive)

# ¿Cual es el precio promedio del boleto para los sobrevivientes?
print("¿Cual es el precio promedio del boleto para los sobrevivientes?")

print("El precio promedio para los pasajeros que sobrevivieron es de",promedio_fare_Survive )

print("¿Cual es el precio promedio del boleto para los que no sobrevivieron?")

print("El precio promedio para los pasajeros que no sobrevivieron es de",promedio_fare_not_survive )