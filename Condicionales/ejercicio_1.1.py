#- Actividad 1.1: Escribir un programa que pida al usuario su edad y le diga si es mayor
#de edad (18 años o más).
# Solicitar al usuario que ingrese su edad
edad = int(input('Ingrese su edad: '));  # Convierte la entrada a un número entero

# Verificar si la edad está en el rango de 18 a 100 años
if edad >= 18 and edad < 100:  # Condición para ser mayor de edad y menor de 100
    print('es mayor de edad');  # Mensaje si cumple la condición

# Verificar si la edad es menor a 18
elif edad < 18:  # Condición para ser menor de edad
    print('es menor de edad');  # Mensaje si es menor de 18

# Manejar casos fuera del rango esperado
else:  # Si la edad no está entre 0 y 100
    print('la edad ingresada no es correcta');  # Mensaje para edades inválidas