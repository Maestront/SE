# -*- coding: utf-8 -*-
"""
Created on Fri May 16 19:33:54 2025

@author: Usuario
"""

import numpy as np
import matplotlib.pyplot as plt

# Generación de una función objetivo: y = 7x + 13y - 34z + 7b
# Se crearán datos sintéticos y se entrenará un modelo lineal para aprender estos coeficientes

# Se generan 100 números enteros aleatorios entre 0 y 9 para cada variable
x1 = np.random.randint(0, 10, 100)
x2 = np.random.randint(0, 10, 100)
x3 = np.random.randint(0, 10, 100)
x4 = np.random.randint(0, 10, 100)

# Cálculo de la salida real y usando la combinación lineal dada
y = 7*x1 + 13*x2 - 34*x3 + 7*x4

n = len(y)  # Número de muestras

# Inicialización de los pesos del modelo (w1, w2, w3, w4)
w1, w2, w3, w4 = 0.0, 0.0, 0.0, 0.0

# Tasa de aprendizaje y número de épocas
alpha = 0.01
epocas = 200

# Arreglo para guardar el error cuadrático medio (MSE) por época
pltmse = np.zeros(epocas)

# Entrenamiento usando descenso del gradiente
for epoca in range(epocas):

    # Predicción usando la combinación lineal de entradas y pesos
    y_pred = w1*x1 + w2*x2 + w3*x3 + w4*x4

    # Cálculo del error entre la predicción y el valor real
    error = y_pred - y

    # Cálculo del gradiente (derivadas parciales respecto a cada peso)
    dw1 = (np.sum(error * x1)) / n
    dw2 = (np.sum(error * x2)) / n
    dw3 = (np.sum(error * x3)) / n
    dw4 = (np.sum(error * x4)) / n

    # Actualización de los pesos
    w1 -= alpha * dw1
    w2 -= alpha * dw2
    w3 -= alpha * dw3
    w4 -= alpha * dw4

    # Cálculo del error cuadrático medio (MSE) de la época actual
    mse = np.mean(error ** 2)
    pltmse[epoca] = mse  # Se guarda el MSE en la lista para graficar

    # Imprimir el MSE actual
    print(f"Epoca: {epoca}, MSE: {mse}")

# Imprimir los pesos finales aprendidos (aproximadamente deberían ser 7, 13, -34, 7)
print("Ecuación aprendida:\n")
print(f"w1: {w1}, w2: {w2}, w3: {w3}, w4: {w4}")

# Gráfica de la evolución del MSE durante el entrenamiento
plt.plot(pltmse)
plt.xlabel("Épocas")
plt.ylabel("Error cuadrático medio (MSE)")
plt.title("Entrenamiento por descenso del gradiente")
plt.grid()
plt.show()
