# -*- coding: utf-8 -*-
"""
Created on Sat May 17 18:09:21 2025

@author: Edmundo
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# 1. Cargar el dataset
df = pd.read_csv('forestfires.csv')

# 2. One-hot encoding para mes y día
df = pd.get_dummies(df, columns=['month', 'day'])

# 3. Separar características y variable objetivo
X = df.drop('area', axis=1).astype(float).values
y = df['area'].astype(float).values

# 4. Normalizar características y variable objetivo
X = (X - X.mean(axis=0)) / X.std(axis=0)
y = (y - y.mean()) / y.std()

# 5. Dividir en entrenamiento y prueba
n = len(y)
n_train = int(n * 0.8)

X_train = X[:n_train]
X_test = X[n_train:]

y_train = y[:n_train]
y_test = y[n_train:]

# 6. Inicializar pesos y sesgo
w = np.zeros(X_train.shape[1])
b = 0.0

tasa_aprendizaje = 0.001
epocas = 500

mse_entrenamiento = []

# 7. Entrenamiento
for epoca in range(epocas):
    y_pred = np.dot(X_train, w) + b
    error = y_pred - y_train

    dw = (2 / len(y_train)) * np.dot(X_train.T, error)
    db = (2 / len(y_train)) * np.sum(error)

    w -= tasa_aprendizaje * dw
    b -= tasa_aprendizaje * db

    mse = np.mean(error**2)
    mse_entrenamiento.append(mse)

    if epoca % 100 == 0:
        print(f"Época {epoca}, MSE entrenamiento: {mse:.6f}")

# 8. Evaluación en test
y_pred_test = np.dot(X_test, w) + b
mse_test = np.mean((y_pred_test - y_test)**2)
print(f"MSE en test: {mse_test:.6f}")

# 9. Graficar error MSE durante el entrenamiento
plt.figure(figsize=(12,5))

plt.subplot(1, 2, 1)
plt.plot(range(epocas), mse_entrenamiento, label='MSE Entrenamiento')
plt.xlabel("Épocas")
plt.ylabel("Error cuadrático medio (MSE)")
plt.title("Evolución del error durante el entrenamiento")
plt.legend()

# 10. Graficar valores reales vs predichos en test
plt.subplot(1, 2, 2)
plt.scatter(y_test, y_pred_test, alpha=0.6, color='blue', label='Predicciones')
plt.plot([-3, 3], [-3, 3], 'r--', label='Ideal y=x')
plt.xlabel("Valores reales (normalizados)")
plt.ylabel("Valores predichos (normalizados)")
plt.title("Valores reales vs valores predichos")
plt.legend()
plt.show()



