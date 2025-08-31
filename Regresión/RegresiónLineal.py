# -*- coding: utf-8 -*-
"""
Created on Thu Apr  3 15:22:35 2025

@author: Usuario
"""

import numpy as np
import matplotlib.pyplot as plt

x = np.arange(-5, 6)
y = np.arange(-10, 12, 2)
n = len(x)
w = np.arange(-5, 6)
Et = np.zeros(len(w))

def Graficar(x, y, w1, n):
    ye = np.zeros(n)
    yd = np.zeros(n)
    E = 0
    
    for i in range(n):
        ye[i] = x[i] * w1
        yd[i] = (y[i] - ye[i]) ** 2
    
    E = np.sum(yd) / (2 * n)
    return E

for i in range(len(w)):
    Et[i] = Graficar(x, y, w[i], n)

plt.plot(w, Et)
plt.xlabel("w")
plt.ylabel("Error")
plt.title("Error vs w")
plt.grid(True)
plt.show()
