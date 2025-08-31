# -*- coding: utf-8 -*-
"""
Created on Wed Feb 12 22:40:22 2025

@author: Edmundo
"""

# Lista para almacenar los libros favoritos
favorite_books = []  

# Se agregan algunos libros a la lista
favorite_books.append("El Señor de los Anillos")
favorite_books.append("La Odisea")
favorite_books.append("La Sombra de la Reina")
favorite_books.append("Los Cuatro Acuerdos")
favorite_books.append("La Canción de Aquiles")

# Función para imprimir la lista de libros
def print_list(books_list):
    for x in books_list:  # Recorre la lista e imprime cada libro
        print(x)

# Función para agregar un nuevo libro a la lista
def add_book(book_name):
    favorite_books.append(book_name)  # Añade el libro a la lista

# Mostrar la lista original de libros
print("Lista original\n")        
print_list(favorite_books)

# Bucle para permitir al usuario agregar libros
while True:
    x = input("\nDesea añadir algún libro a la lista? y/n\n")  # Pregunta al usuario
    if x == "y" or x == "Y":  # Si responde "y" (sí), pide el nombre del libro
        book_name = input("Ingrese el nombre del libro:\n")
        add_book(book_name)  # Agrega el libro a la lista
    elif x == "n" or x == "N":  # Si responde "n" (no), finaliza el bucle
        break
    else:
        print("Ingrese una opción válida\n")  # Mensaje de error si la entrada no es válida

# Mostrar la lista final con los libros añadidos
print("\nLista final\n")
print_list(favorite_books)
