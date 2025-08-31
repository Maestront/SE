# -*- coding: utf-8 -*-
"""
Created on Fri Apr  4 19:25:26 2025

@author: Usuario
"""

import numpy as np

n = 0.5 #Eta, tasa de aprendizaje

x0 = np.array([1,1,1,1])
x1 = np.array([-1,1,-1,1])
x2 = np.array([-1,-1,1,1])
y = np.array([-1,-1,-1,1])

w = np.array([1,1,1])

def Perceptron(n,x0,x1,x2,y,w):
    
    i = -1

    a = 1
    
    while True:
        i += 1
        x = np.array([x0[i],x1[i],x2[i]])
        z = np.dot(w,x)
    
        ye = np.sign(z)
        
        E = y[i] - ye
        
        w = w + (n*(y[i]-ye)*x)
        
        if E == 0 and i == 3:
            break;
        
        if i == 3:
            i = -1
            a += 1
    
    return w

def Prueba(w, x0, x1, x2, y):
    print("{:<5} {:<5} {:<5} {:<5} {:<5}".format("X0", "X1", "X2", "Ye-", "E"))
    for i in range(len(x0)):
        E = False
        x = np.array([x0[i], x1[i], x2[i]])
        r = np.sign(np.dot(w, x))

        if y[i] == r:
            E = True

        # Aquí usamos f-string para un formato alineado
        print(f"{x0[i]:<5} {x1[i]:<5} {x2[i]:<5} {np.int64(r):<5} {E:<5}")
        
wf = Perceptron(n, x0, x1, x2, y, w)

Prueba(wf, x0, x1, x2,y)
    
    
    