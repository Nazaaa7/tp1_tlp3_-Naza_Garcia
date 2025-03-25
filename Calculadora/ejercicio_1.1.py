#Actividad 1.1: Los estudiantes deben crear una calculadora básica que permita realizar operaciones de suma, resta, multiplicación y división con entradas del usuario. El programa debe pedir al usuario que elija la operación y luego introducir 2 números para realizar el cálculo.

# Calculadora básica en Python

# Mostramos las opciones de operación al usuario
print("Seleccione una operación:")
print("1. Suma")
print("2. Resta")
print("3. Multiplicación")
print("4. División")

# Solicitamos la opción al usuario
opcion = input("Ingrese el número de la operación que desea realizar: ")

# Pedimos los dos números que se usarán en la operación
num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))

# Verificamos la operación seleccionada y realizamos el cálculo correspondiente
if opcion == "1":
    resultado = num1 + num2  # Suma
    print(f"La suma de {num1} + {num2} es: {resultado}")
elif opcion == "2":
    resultado = num1 - num2  # Resta
    print(f"La resta de {num1} - {num2} es: {resultado}")
elif opcion == "3":
    resultado = num1 * num2  # Multiplicación
    print(f"La multiplicación de {num1} * {num2} es: {resultado}")
elif opcion == "4":
    if num2 != 0:  # Verificamos que el segundo número no sea cero para evitar error
        resultado = num1 / num2  # División
        print(f"La división de {num1} / {num2} es: {resultado}")
    else:
        print("Error: No se puede dividir entre cero.")  # Mensaje de error si num2 es 0
else:
    print("Opción inválida. Por favor, seleccione una operación válida.")  # Mensaje si la opción no es 1-4
