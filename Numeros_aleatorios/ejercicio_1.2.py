#- Actividad 1.2: Sumar los 5 números generados aleatoriamente y en caso de que el
# resultado sea mayor a 100, mostrar el valor antes de ser mayor a 100 y cuántos
# números se sumaron para llegar a dicho valor.
import random

# inicializa la suma de los números
suma_total = 0
cantidad_numeros = 0

# genera y suma 5 números aleatorios entre 1 y 100
for i in range(5):
    numero = random.randint(1, 100)  # Genera un número aleatorio entre 1 y 100
    suma_total += numero  # Sumar el número generado a la suma total
    cantidad_numeros += 1  # Contar cuántos números se han sumado

    # Verificar si la suma ya supera 100
    if suma_total > 100:
        print(f"Suma antes de exceder 100: {suma_total - numero}")
        print(f"Se sumaron {cantidad_numeros - 1} números antes de que la suma fuera mayor a 100.")
        break  # Termina el bucle si la suma excede 100
else:
    # Si la suma no excede 100 después de sumar 5 números
    print(f"Suma total de los 5 números: {suma_total}")