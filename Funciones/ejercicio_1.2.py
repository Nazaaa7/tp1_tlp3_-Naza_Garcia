# - Actividad 1.2: Crear una función que reciba dos números y devuelva su suma, resta,
# multiplicación y división.
def operaciones(a, b):  # a y b (parametros para la funcion)
    suma = a + b
    resta = a - b
    multiplicacion = a * b
    
    # verificamos que b no sea 0 para evitar error de división por cero
    if b != 0:
        division = a / b
    else:
        division = "No se puede dividir por 0"
    
    # Devolvemos los resultados directamente
    return suma, resta, multiplicacion, division

# Llamamos a la función con dos números
suma, resta, multiplicacion, division = operaciones(100, 7)

# imprimimos los resultados
print(f"Suma: {suma}")
print(f"Resta: {resta}")
print(f"Multiplicación: {multiplicacion}")
print(f"División: {division}")