# -*- coding: utf-8 -*-
"""
Created on Wed Feb 12 23:34:33 2025

@author: Edmundo
"""

# Tupla que almacena los países que se quieren visitar
countries_to_visit = ("Japon", "Alemania", "Canada")

# Función para imprimir la lista de países
def print_countries():
    for x in countries_to_visit:  # Recorre la tupla e imprime cada país
        print(x)

# Función para buscar un país en la lista
def find_country(country):
    c = 0  # Variable para indicar si se encontró el país
    for x in countries_to_visit:  # Recorre la tupla
        if x == country:  # Compara si el país está en la lista
            print("\nEl país SÍ se encuentra en la lista\n")
            c = 1  # Indica que el país fue encontrado
            break  # Termina la búsqueda
    if c == 0:  # Si no se encontró el país
        print("\nEl país NO se encuentra en la lista\n")

# Bucle principal para buscar países en la lista
while True:
    x = input("\n¿Desea buscar algún país en la lista? y/n\n")  # Pregunta al usuario
    if x == "y" or x == "Y":  # Si responde "y", solicita el país a buscar
        country = input("Ingrese el país a buscar:\n")
        find_country(country)  # Llama a la función para buscar el país
    elif x == "n" or x == "N":  # Si responde "n", termina el programa
        break
    else:
        print("Ingrese una opción válida\n")  # Mensaje de error si la entrada no es válida

# Muestra la lista de países al final
print("\nLista:\n")
print_countries()
