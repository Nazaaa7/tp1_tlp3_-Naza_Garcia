#Actividad 1.2: Implementar una opción para que el usuario pueda continuar haciendo
#cálculos o salir del programa.

while True:  # Bucle infinito hasta que el usuario decida salir
    # Mostramos las opciones de operación al usuario
    print("\nSeleccione una operación:")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")
    print("5. Salir")  # Nueva opción para salir

    # Solicitamos la opción al usuario
    opcion = input("Ingrese el número de la operación que desea realizar: ")

    # Si el usuario elige la opción 5, salimos del bucle
    if opcion == "5":
        print("Gracias por usar la calculadora. ¡Hasta luego!")
        break

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
        print("Opción inválida. Por favor, seleccione una operación válida.")  # Mensaje si la opción no es 1-5
