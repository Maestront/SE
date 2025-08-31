# -*- coding: utf-8 -*-
"""
Created on Sat Mar 15 21:28:52 2025

@author: Edmundo
"""

columna = {}
columna[1] = 0
fila = 1
k = 1

while k > 0 and k < 5:
    columna[k] = columna[k] + 1
    ciclo = True
    while columna[k] <= 4 and k > 1 and ciclo:
        ciclo = False
        for x in columna:
            dif = k - x
            EvaDiagoInf = False
            EvaDiagoInf = (columna[k-dif] == (columna[k] + dif))
            EvaDiagoSup = False
            EvaDiagoSup = (columna[k-dif] == (columna[k] - dif))
            EvaFila = False
            EvaFila = (columna[x] == columna[k])
            
            if x < k and EvaDiagoInf or EvaDiagoSup or EvaFila:
                columna[k] = columna[k] + 1
                ciclo = True
        
    if columna[k] > 4:
        k = k - 1
        
    else:
        k = k + 1
        if k < 5:
            columna[k] = 0