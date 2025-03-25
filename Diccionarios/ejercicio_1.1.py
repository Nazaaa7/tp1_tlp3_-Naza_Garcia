#Actividad 1.1: Crear un diccionario que contenga los nombres de tres personas como
# claves y sus edades como valores. El programa debe imprimir la edad de cada
# persona.

# En Python, un diccionario es una colección de elementos no ordenados,
# mutables (es decir, podemos cambiar sus valores después de crearlos) y
# indexados por claves únicas. Los diccionarios se definen usando {} y cada 
# elemento se representa como un par clave-valor.

personas = {
    "Juan": 15,
    "Cami": 25,
    "Pepe": 50
}

# Imprimir la edad de cada persona, accediendo a la clave, mostrando el valor
print("juan:", personas["Juan"])
print("cami:", personas["Cami"])
print("pepe:", personas["Pepe"])