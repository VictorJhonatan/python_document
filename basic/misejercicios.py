### EJERCICIOS DE PYTHON BASICO -

# Ejercicio 1: 
"""Escribe un programa que solicite 
al usuario su nombre y edad,y luego 
imprima un mensaje que diga "Hola [nombre], tienes [edad] años"."""

def greet_user():
    name = input("Ingresa tu nombre: ")
    age = input("Ingresa tu edad: ")
    print(f"Hola {name}, tienes {age} años.")

# Ejercicio 2: 
"""Escribe un programa que calcule 
el área de un rectángulo."""

def calculate_rectangle_area( width, height):
    area = width * height
    return area
    
dato_width = float(input("Ingresa el ancho del rectángulo: "))
dato_height = float(input("Ingresa la altura del rectángulo: "))

area_result = calculate_rectangle_area(dato_width, dato_height)
print(f"El área del rectángulo es: {area_result}")
print()

# EJERCICIO 3:
"""Cuenta cuantas veces aparece 
un elemento en una lista usando 
el metodo count()"""

def ejercicio3(inputlist, inputelement):

    cuent = inputlist.count(inputelement)
    return cuent

dato_list = input("Ingresa elementos en la lista: ").split() # separa los elementos por espacios y los convierte en una lista
dato_element = input("Ingresa el elemento a buscar en la lista: ")

dato = ejercicio3(dato_list, dato_element)
print(f"EL elemento: '{dato_element}': su Ocurrencia es: {dato}")

# Ejercicio 4:
"""Encuentra la longitud de una 
lista usando la funcion len()"""

def ejercicio4(inputlist):
    longitud = len(inputlist)
    return longitud

dato_list2 = input("Ingresa elementos en la lista: ").split() # separa los elementos por espacios y los convierte en una lista
longitud_result = ejercicio4(dato_list2)
print(f"La longitud de la lista es: {longitud_result}")

#len s



    
