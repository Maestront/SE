# -*- coding: utf-8 -*-
"""
Created on Sat May 17 16:40:35 2025

@author: Edmundo
"""

import numpy as np
import matplotlib.pyplot as plt

# Cargar datos
datos = np.loadtxt('wine.data', delimiter=',')
y = datos[:, 0].astype(int)
X = datos[:, 1:]

# Filtrar clases 1 y 2
indices = (y == 1) | (y == 2)
X = X[indices]
y = (y[indices] == 2).astype(int)  # Clase 2 -> 1, Clase 1 -> 0

# Dividir datos
n = len(y)
idx = np.arange(n)
np.random.shuffle(idx)

train_size = int(0.7 * n)
train_idx, test_idx = idx[:train_size], idx[train_size:]

X_train, y_train = X[train_idx], y[train_idx]
X_test, y_test = X[test_idx], y[test_idx]

# Normalización
media = X_train.mean(axis=0)
desv = X_train.std(axis=0)
X_train = (X_train - media) / desv
X_test = (X_test - media) / desv

# Mostrar ejemplos reales antes del entrenamiento
print("Ejemplos reales (antes del entrenamiento):")
for i in range(5):
    print(f"Entrada: {X_test[i]}, Etiqueta real: {y_test[i]}")
print()

# Función sigmoide
def sigmoide(z):
    z = np.clip(z, -500, 500)
    return 1 / (1 + np.exp(-z))

# Entrenamiento
def entrenar(X, y, lr=0.1, epocas=1000, tol=1e-6):
    m, n = X.shape
    w = np.zeros(n)
    b = 0
    costos = []
    print("Entrenamiento:\n")
    for i in range(epocas):
        z = np.dot(X, w) + b
        y_pred = sigmoide(z)
        error = y_pred - y

        dw = (1/m) * np.dot(X.T, error)
        db = (1/m) * np.sum(error)

        w -= lr * dw
        b -= lr * db

        costo = -np.mean(y*np.log(y_pred + 1e-15) + (1-y)*np.log(1 - y_pred + 1e-15))
        costos.append(costo)

        if i % 100 == 0:
            print(f"Época {i}: costo = {costo:.6f}")
        if i > 0 and abs(costos[-2] - costo) < tol:
            print(f"Convergencia alcanzada en la época {i}")
            break
    print(f"W: {w}, b: {b}\n")
    return w, b, costos

# Predicción
def predecir(X, w, b):
    return (sigmoide(np.dot(X, w) + b) >= 0.5).astype(int)

# Entrenar modelo
w, b, costos = entrenar(X_train, y_train)

# Evaluación final
y_pred = predecir(X_test, w, b)
exactitud = np.mean(y_pred == y_test)
print(f"Exactitud en test: {exactitud * 100:.2f}%\n")

# Gráfica 1: Costo por época (ya la tienes, la dejamos igual o con mejoras)
plt.figure(figsize=(12, 5))

plt.subplot(1, 2, 1)
plt.plot(costos, color='blue')
plt.xlabel('Épocas')
plt.ylabel('Costo (log-loss)')
plt.title('Evolución del costo durante entrenamiento')

# Gráfica 2: Valores reales vs predichos
plt.subplot(1, 2, 2)
plt.scatter(range(len(y_test)), y_test, label='Real', color='green', alpha=0.6)
plt.scatter(range(len(y_test)), y_pred, label='Predicho', color='red', marker='x', alpha=0.6)
plt.xlabel('Índice de muestra')
plt.ylabel('Clase')
plt.title('Comparación entre valores reales y predichos')
plt.legend()

plt.tight_layout()
plt.show()


# Mostrar ejemplos después del entrenamiento
print("Ejemplos con predicción (después del entrenamiento):")
for i in range(5):
    pred = predecir(X_test[i].reshape(1, -1), w, b)[0]
    print(f"Entrada: {X_test[i]}")
    print(f"Etiqueta real: {y_test[i]} -> Predicción: {pred}\n")


