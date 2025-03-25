#- Actividad 1.2: Escribir un programa que pregunte al usuario un nombre, luego su
# edad y los agregue al diccionario.
nombre = input('Ingrese su nombre: ')  # variable para ingresar el nombre
edad = int(input('Ingrese su edad: '))  # variable para ingresar la edad
personas = {}  # inicializar el diccionario vacío

personas[nombre] = edad  # se agregan las claves y valores al diccionario
print(personas)  # se imprime en la consola el diccionario