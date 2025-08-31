# -*- coding: utf-8 -*-
"""
Created on Fri Mar 21 19:30:21 2025

@author: Edmundo
"""

import math

class Nodo:
    def __init__(self, posicion, padre=None): 
        self.posicion = posicion  # (x, y)
        self.padre = padre        # Nodo anterior o nodo padre
        self.g = 0                # Costo desde el inicio
        self.h = 0                # Costo heurístico estimado para la meta
        self.f = 0                # Costo total siendo h+g

    def __lt__(self, otro):
        return self.f < otro.f  # Función para comparar dos nodos

def heuristico(posicionActual, posicionMeta):
    x1, y1 = posicionActual
    x2, y2 = posicionMeta
    
    # Método euclidiano para tomar en cuenta movimientos en diagonal
    estimado = math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
    
    return estimado

def AStar(mapa, inicio, final):
    filas = len(mapa)
    columnas = len(mapa[0])
    
    nodoInicial = Nodo(inicio)
    nodoInicial.g = 0
    nodoInicial.h = heuristico(inicio, final)
    nodoInicial.f = nodoInicial.g + nodoInicial.h
    
    listaAbierta = []  # Lista para nodos no visitados
    listaAbierta.append(nodoInicial)  # Añadimos el nodo de inicio a los nodos todavía no visitados
    listaCerrada = []  # Lista para nodos visitados
    
    movimientos = [(0, -1), (0, 1), (1, 0), (-1, 0)]  # Movimientos: izquierda, derecha, abajo, arriba
    
    while listaAbierta:
        nodoActual = min(listaAbierta, key=lambda n: n.f)  # Buscamos el nodo con menor f en la lista abierta
        listaAbierta.remove(nodoActual)  # Eliminamos el nodoActual de la lista abierta
        
        if nodoActual.posicion == final:  # Si llegamos al objetivo
            ruta = []
            while nodoActual:
                ruta.append(nodoActual.posicion)
                nodoActual = nodoActual.padre
            return ruta[::-1]  # Devolvemos la ruta desde el inicio hasta el final
        listaCerrada.append(nodoActual.posicion)
        
        for movimiento in movimientos:
            xActual, yActual = nodoActual.posicion[0] + movimiento[0], nodoActual.posicion[1] + movimiento[1]
            if 0 <= xActual < filas and 0 <= yActual < columnas and mapa[xActual][yActual] == 0:
                vecino = Nodo((xActual, yActual), nodoActual)
                if vecino.posicion in listaCerrada:
                    continue
                
                vecino.g = nodoActual.g + 1
                vecino.h = heuristico(vecino.posicion, final)
                vecino.f = vecino.g + vecino.h
                
                if any(n.posicion == vecino.posicion and n.f <= vecino.f for n in listaAbierta):
                    continue
                
                listaAbierta.append(vecino)
    
    return 0  # Si no se encuentra una solución

def visualizar_camino(mapa, camino):
    mapa_visualizado = [fila[:] for fila in mapa]  # Copiar el mapa original para no modificarlo
    for x, y in camino:
        mapa_visualizado[x][y] = '*'  # Marcamos el camino con 2
    return mapa_visualizado

def imprimir_mapa(mapa):
    for fila in mapa:
        print(" ".join(str(celda) for celda in fila))

# Tres mapas con diferentes dificultades
mapas = [
    [
        [0, 0, 1, 0, 0],
        [1, 0, 1, 0, 0],
        [1, 0, 0, 1, 0],
        [0, 1, 0, 0, 0],
        [0, 0, 0, 1, 0]
    ],  # Mapa 1
    [
        [0, 0, 1, 0, 0, 0, 0],
        [1, 0, 1, 1, 1, 0, 0],
        [1, 0, 0, 0, 1, 0, 0],
        [0, 1, 1, 0, 1, 1, 0],
        [0, 0, 0, 0, 0, 1, 0],
        [0, 1, 1, 1, 1, 1, 0],
        [0, 0, 0, 0, 0, 0   , 0]
    ],  # Mapa 2
    [
        [0, 0, 1, 0, 0, 0, 1, 0, 1, 0],
        [1, 0, 1, 0, 1, 0, 0, 0, 0, 0],
        [1, 0, 0, 0, 0, 1, 0, 1, 1, 0],
        [0, 0, 1, 1, 0, 0, 1, 0, 0, 0],
        [0, 1, 1, 0, 1, 0, 1, 1, 0, 0],
        [1, 0, 1, 0, 0, 0, 0, 1, 1, 0],
        [0, 1, 0, 0, 1, 0, 0, 1, 0, 0],
        [1, 0, 0, 1, 0, 1, 0, 0, 0, 0],
        [0, 0, 1, 1, 1, 0, 0, 0, 1, 0],
        [0, 0, 0, 0, 0, 0, 1, 0, 0, 0]
    ]  # Mapa 3
]


# Iteramos sobre cada mapa
for i, mapa in enumerate(mapas):
    print(f"Mapa {i + 1}:\n")
    
    # Ejecutamos el algoritmo A* y obtenemos el camino
    camino = AStar(mapa, (0, 0), (len(mapa)-1, len(mapa[0])-1))  # Asumiendo que la meta es la esquina inferior derecha
    
    if camino == 0:
        print("No se encontró una solución")
    else:
        print("Se encontró una solución:\n")
        mapa_con_camino = visualizar_camino(mapa, camino)
        imprimir_mapa(mapa_con_camino)
    
    print()  # Espacio entre mapas para mejor legibilidad







