# -*- coding: utf-8 -*-
"""
Created on Wed Feb 12 23:10:49 2025

@author: Edmundo
"""

# Diccionario que almacena nombres de amigos y sus edades
friends_info = {"Eric": "33", "Cesar": "20", "Ketzel": "21"}

# Función para imprimir la información del diccionario
def print_info(friends_info):
    for x, y in friends_info.items():  # Recorre cada clave (nombre) y valor (edad)
        print(f"{x} tiene {y} años\n")

# Función para actualizar la edad de un amigo en el diccionario
def change_age(name):
    age = input("\nIngrese la edad actualizada:\n")  # Solicita la nueva edad
    friends_info[name] = age  # Actualiza la edad en el diccionario

# Mostrar el diccionario original
print("Diccionario Original\n")
print_info(friends_info)

# Bucle para permitir la actualización de edades
while True:
    x = input("\nDesea actualizar alguna edad? y/n\n")  # Pregunta al usuario
    if x == "y" or x == "Y":  # Si responde "y", pide el nombre a actualizar
        name = input("Ingrese el nombre de la persona a actualizar la edad:\n")
        if name in friends_info:  # Verifica si el nombre existe en el diccionario
            change_age(name)  # Llama a la función para actualizar la edad
            print("\nDiccionario Actualizado\n")
            print_info(friends_info)  # Muestra el diccionario actualizado
        else:
            print("\nEl nombre ingresado no está en la lista.\n")
    elif x == "n" or x == "N":  # Si responde "n", finaliza el bucle
        break
    else:
        print("Ingrese una opción válida\n")  # Mensaje de error si la entrada no es válida

# Mostrar el diccionario final con los cambios realizados
print("Diccionario Final\n")
print_info(friends_info)
