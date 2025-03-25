# Actividad 1.2: Usar un bucle para calcular la suma de los números de la lista.
nums = [10, 20, 30, 40, 50]  #lista
suma = 0  # variable para la suma de los elementos de la lista

for num in nums:  # Recorremos cada número en la lista
    suma = suma + num  # sumamos los numeros, en cada iteración, el número actual (num) se suma al valor de suma

print("el resultado de la suma es:", suma)  # se imprime La suma fuera del bucle