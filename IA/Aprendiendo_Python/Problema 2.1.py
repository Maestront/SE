# -*- coding: utf-8 -*-
"""
Created on Fri Feb 14 12:48:20 2025

@author: Edmundo
"""

class BankAccount:
    def __init__(self):  # Constructor de la clase
        self.saldo = 0  # Inicializa el saldo en 0
    
    def deposit(self, amount):  # Método para depositar dinero
        self.saldo += amount  # Suma la cantidad al saldo
        return self.saldo  # Retorna el nuevo saldo
    
    def withdraw(self, amount):  # Método para retirar dinero
        if amount > self.saldo:  # Verifica si hay saldo suficiente
            print("\nSaldo insuficiente\n")
            return self.saldo  # No cambia el saldo si no hay suficiente dinero
        self.saldo -= amount  # Resta la cantidad al saldo si es posible
        return self.saldo  # Retorna el nuevo saldo
    
    def get_balance(self):  # Método para obtener el saldo actual
        return self.saldo  # Devuelve el saldo

# Crear una cuenta bancaria
cuenta = BankAccount()

# Bucle principal para interactuar con el usuario
while True:
    # Menú de opciones
    x = input("Qué operación desea realizar?\n1-Depositar\n2-Retirar\n3-Saldo\n0-Salir\n")
    
    if x == "1" or x == "2":  # Si el usuario elige depositar o retirar
        amount = input("Ingresa la cantidad:\n")
        
        try:
            amount = float(amount)  # Intenta convertir la entrada en un número
            if amount <= 0:  # Verifica que el monto sea válido
                print("Ingrese una cantidad válida mayor a 0.")
                continue  # Vuelve a pedir la entrada si el monto no es válido
        except ValueError:
            print("\nIngrese un número válido.")  # Mensaje si la conversión falla
            continue  # Vuelve a pedir la entrada
        
        if x == "1":  # Si la opción es "Depositar"
            cuenta.deposit(amount)  # Llama al método deposit
            print("\nOperación realizada\n")
        else:  # Si la opción es "Retirar"
            cuenta.withdraw(amount)  # Llama al método withdraw
            print("\nOperación realizada\n")

    elif x == "3":  # Si el usuario quiere consultar el saldo
        print(f"\nEl saldo es de: {cuenta.get_balance()}\n")  # Muestra el saldo actual

    elif x == "0":  # Si el usuario elige salir
        break  # Rompe el bucle y finaliza el programa

    else:  # Si el usuario ingresa una opción inválida
        print("\nIngrese una opción válida\n")  # Mensaje de error

