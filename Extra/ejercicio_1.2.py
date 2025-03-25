#- Actividad 1.2: Limitar el número de intentos y mostrar un mensaje de éxito o fracaso
# al final.
import random  # importa la librería random para generar números aleatorios

# genera un número aleatorio entre 1 y 100
numero_secreto = random.randint(1, 100)

# define el número máximo de intentos permitidos
intentos_maximos = 5

# inicializa la variable para almacenar la suposición del usuario
intento = None

# inicializa el contador de intentos en 0
intentos_realizados = 0

# inicia un bucle que se ejecuta hasta que el usuario acierte o se quede sin intentos
while intentos_realizados < intentos_maximos:
    # pide al usuario que ingrese un número y lo convierte en entero
    intento = int(input(f"Intento {intentos_realizados + 1}/{intentos_maximos}. Adivina el número entre 1 y 100: "))

    # aumenta el contador de intentos en 1
    intentos_realizados += 1

    # verifica si el número ingresado es mayor al número secreto
    if intento > numero_secreto:
        print("El número es menor. Intenta de nuevo.")  # da una pista al usuario
    # verifica si el número ingresado es menor al número secreto
    elif intento < numero_secreto:
        print("El número es mayor. Intenta de nuevo.")  # da otra pista al usuario
    else:
        # si el usuario acierta, muestra un mensaje y termina el juego
        print(f"¡Felicidades! Adivinaste el número {numero_secreto} en {intentos_realizados} intentos.")
        break  # sale del bucle porque ya acertó

# si el usuario agotó todos los intentos y no adivinó, muestra un mensaje de fracaso
if intento != numero_secreto:
    print(f"Lo siento, te quedaste sin intentos. El número era {numero_secreto}.")
