# -*- coding: utf-8 -*-
"""
Created on Sat May 17 16:38:37 2025

@author: Edmundo
"""

import numpy as np
import matplotlib.pyplot as plt

# Entradas y salidas XOR
X = np.array([[0,0],
              [0,1],
              [1,0],
              [1,1]])

y = np.array([[0],[1],[1],[0]])

def sigmoide(x):
    return 1/(1+np.exp(-x))

def d_sigmoide(x):
    return x*(1-x)

np.random.seed(42)
e_in = 2     # tamaño entrada
e_oc = 2     # tamaño capa oculta
e_out = 1    # tamaño salida

# pesos iniciales (entrada->oculta y oculta->salida)
W1 = np.random.randn(e_in, e_oc)*0.1
W2 = np.random.randn(e_oc, e_out)*0.1

alpha = 0.3          # tasa de aprendizaje
ep_max = 1000000      # máximo épocas
mse_umbral = 1e-5    # error umbral

mse_hist = []
mse = float('inf')
epoca = 0

while mse > mse_umbral and epoca < ep_max:
    # forward
    z1 = np.dot(X, W1)
    a1 = sigmoide(z1)
    z2 = np.dot(a1, W2)
    a2 = sigmoide(z2)

    # error
    err = y - a2
    mse = np.mean(err**2)
    mse_hist.append(mse)

    # backprop
    delta2 = err * d_sigmoide(a2)
    dW2 = np.dot(a1.T, delta2)

    delta1 = delta2.dot(W2.T) * d_sigmoide(a1)
    dW1 = np.dot(X.T, delta1)

    # actualizar pesos
    W1 += alpha * dW1
    W2 += alpha * dW2

    # Mostrar avance cada 5000 épocas
    if epoca % 5000 == 0:
        print(f"Época {epoca}, MSE: {mse:.6f}")

    epoca += 1

print(f"\nEntrenamiento finalizado en {epoca} épocas con MSE = {mse:.6f}\n")

# Resultados
print("Resultados finales:")
for i in range(len(X)):
    pred = sigmoide(np.dot(sigmoide(np.dot(X[i], W1)), W2))
    print(f"Entrada: {X[i]} -> Esperado: {y[i][0]} -> Predicho: {pred[0]:.4f}")

# Gráfica de error
plt.plot(mse_hist)
plt.title("Error cuadrático medio (MSE)")
plt.xlabel("Épocas")
plt.ylabel("MSE")
plt.grid(True)
plt.show()
