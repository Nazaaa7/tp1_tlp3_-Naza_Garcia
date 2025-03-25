#- Actividad 1.2: Usar un bucle `while` para imprimir los números del 1 al 10, e
# imprimir solo aquellos números que sean divisibles por 2.
num = 1  # inicializar en 1

while num <= 10:  # mientras el número sea menor o igual a 10
    if num % 2 == 0:  # si es divisible por 2
        print(num)  # se imprime número que cumpla la condición
    num += 1  # en cada iteración se suma 1