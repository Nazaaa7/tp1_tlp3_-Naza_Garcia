# #- Actividad 1.1: Escribir una función llamada `saludo` que reciba un nombre como
# parámetro y devuelva un saludo personalizado.

def saludar(nombre):
    return f"Hola, {nombre}"  # devuelve el saludo como resultado, (f) forma de incluir expresiones dentro de una cadena de manera sencilla y legible. La variable nombre se inserta directamente en la cadena

# Llamamos la función y guardamos el saludo en una variable
mensaje = saludar("Naza")  # Llama la función y guarda el saludo

# Imprimimos el saludo almacenado en la variable
print(mensaje)  # muestra el saludo por la consola