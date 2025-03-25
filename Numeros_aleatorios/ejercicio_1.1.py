#Actividad 1.1: Escribir un programa que genere 5 números aleatorios entre 1 y 100, lo
# imprima por consola y diga si es mayor o menor a 50.

import random  # Importar el módulo random

# genera 5 números aleatorios entre 1 y 100
for i in range(5):
    numero = random.randint(1, 100)  # Genera un número entero aleatorio entre 1 y 100
    print(f"numero generado: {numero}")  # imprime en la consola el número generado

    # Verificar si el número es mayor o menor que 50
    if numero > 50:
        print("Es mayor que 50")
    else:
        print("Es menor o igual a 50")