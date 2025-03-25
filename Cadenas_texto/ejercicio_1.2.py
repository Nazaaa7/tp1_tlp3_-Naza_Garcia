#- Actividad 1.2: Hacer que el programa imprima la longitud del nombre ingresado (no
# tener en cuenta los espacios en blanco).

nombre = input('Ingrese su nombre: ')

# Eliminamos los espacios en blanco y calculamos la longitud del nombre
nombre_sin_espacios = nombre.replace(" ", "")  # El método replace elimina todos los espacios en blanco del nombre ingresado.

longitud = len(nombre_sin_espacios)  # Calculamos la longitud sin contar los espacios

# Imprimimos la longitud del nombre sin espacios
print("Longitud del nombre: ", longitud)