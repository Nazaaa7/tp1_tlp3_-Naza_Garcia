#- Actividad 1.2: Agregar un mensaje diferente para diferentes rangos de edad, como por
#ejemplo, si es un niño, adolescente o adulto.
# Solicitar al usuario que ingrese su edad
edad = int(input('Ingrese su edad: '));  # Convierte la entrada a un número entero

# Verificar si es un adulto (entre 18 y 100 años)
if edad >= 18 and edad < 100:  # Condición para ser mayor de edad
    print('es un adulto');  # Mensaje si es adulto

# Verificar si es un adolescente (entre 12 y 18 años)
elif edad >= 12 and edad < 18:  # Condición para ser adolescente
    print('es un adolescente');  # Mensaje si es adolescente

# Verificar si es un niño (entre 6 y 12 años)
elif edad > 6 and edad < 12:  # Condición para ser niño
    print('es un niño');  # Mensaje si es niño

# Manejar casos fuera del rango esperado
else:  # Si la edad no está en los rangos definidos
    print('la edad ingresada no es correcta');  # Mensaje para edades inválidas