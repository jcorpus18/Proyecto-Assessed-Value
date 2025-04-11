
# Importación de librerías
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score

# Paso 1: Carga de datos
df = pd.read_csv('datos_propiedades.csv')  # Cambia por tu archivo real
df['Date Recorded'] = pd.to_datetime(df['Date Recorded'])

# Paso 2: Exploración inicial
print(df.info())
print(df.describe())
print(df.isnull().sum())

# Paso 3: Análisis exploratorio de datos
sns.histplot(df['Assessed Value'], kde=True, bins=50)
plt.title('Distribución del Valor Evaluado (Assessed Value)')
plt.xlabel('Assessed Value')
plt.ylabel('Frecuencia')
plt.show()

sns.histplot(df['Sale Amount'], kde=True, bins=50)
plt.title('Distribución del Precio de Venta (Sale Amount)')
plt.xlabel('Sale Amount')
plt.ylabel('Frecuencia')
plt.show()

sns.scatterplot(x='Assessed Value', y='Sale Amount', data=df)
plt.title('Relación Assessed Value vs Sale Amount')
plt.xlabel('Assessed Value')
plt.ylabel('Sale Amount')
plt.show()

corr_matrix = df[['Assessed Value', 'Sale Amount']].corr()
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm')
plt.title('Matriz de Correlación')
plt.show()

# Paso 4: Análisis por localidad
town_analysis = df.groupby('Town')[['Assessed Value', 'Sale Amount']].mean().sort_values(by='Sale Amount', ascending=False)
town_analysis.plot(kind='bar', figsize=(12, 6))
plt.title('Promedio Assessed Value y Sale Amount por localidad')
plt.ylabel('Promedio de Valores')
plt.xlabel('Localidad')
plt.xticks(rotation=45)
plt.show()

# Paso 5: Modelo predictivo
X = df[['Assessed Value']]
y = df['Sale Amount']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

model = LinearRegression()
model.fit(X_train, y_train)
y_pred = model.predict(X_test)

print(f'MSE: {mean_squared_error(y_test, y_pred):.2f}')
print(f'R^2: {r2_score(y_test, y_pred):.2f}')

plt.scatter(X_test, y_test, color='blue', label='Datos reales')
plt.plot(X_test, y_pred, color='red', linewidth=2, label='Predicciones')
plt.title('Modelo de regresión: Assessed Value vs Sale Amount')
plt.xlabel('Assessed Value')
plt.ylabel('Sale Amount')
plt.legend()
plt.show()
