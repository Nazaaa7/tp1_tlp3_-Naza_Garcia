# - Actividad 1.1: Escribir un juego donde el programa elija un número aleatorio entre 1
# y 100 y el usuario tenga que adivinarlo. El programa debe dar pistas si el número es
# mayor o menor.
import random  # importa la librería random para generar números aleatorios

# genera un número aleatorio entre 1 y 100
numero_secreto = random.randint(1, 100)

# inicializa la variable para almacenar la suposición del usuario
intento = None #None es un valor especial que representa la ausencia de un valor o un valor nulo.

# inicia un bucle que se ejecuta hasta que el usuario adivine el número
while intento != numero_secreto:
    # pide al usuario que ingrese un número y lo convierte en entero
    intento = int(input("Adivina el número entre 1 y 100: "))

    # verifica si el número ingresado es mayor al número secreto
    if intento > numero_secreto:
        print("El número es menor. Intenta de nuevo.")  # da una pista al usuario
    # verifica si el número ingresado es menor al número secreto
    elif intento < numero_secreto:
        print("El número es mayor. Intenta de nuevo.")  # da otra pista al usuario

# cuando el usuario acierta, sale del bucle y muestra el mensaje de felicitaciones
print(f"¡Felicidades! Adivinaste el número {numero_secreto}.")
