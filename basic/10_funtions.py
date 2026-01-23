""" Funciones en Python
Una funcion es un bloque de codigo reutilizable que realiza una tarea especifica.

Las funciones en Python se definen utilizando la palabra clave 'def', 
seguida del nombre de la funcion y paréntesis que pueden incluir parametros.

Las fuciones pueden recibir codigos de entrada (parametros) y 
pueden devolver valores utilizando la palabra clave 'return'."""

def mi_funcion():
    """Esta es una funcion simple que no recibe parametros y no devuelve nada."""
    print("Hola desde mi_funcion")   


mi_funcion()  # Llamada a la funcion         


"""Aqui esta funtion ejecuta e imprime pero no devuelve nada"""
def sum_two_values(first_number, second_number):
    """Esta funcion recibe dos parametros y devuelve su suma."""
    print(first_number + second_number)

sum_two_values(5, 7)  # Llamada a la funcion con argumentos


def sum_two_values_with_return(first_value, second_value):
    """Esta funcion recibe dos parametros y devuelve su suma."""
    return first_value + second_value ### return devuelve el valor de la suma

###creo una variable para almacenar el valor devuelto por la funcion
my_result = sum_two_values_with_return(10, 20)  # Llamada a la funcion con argumentos
print("El resultado de la suma es:", my_result)  # Imprime el valor devuelto por la funcion
print(type(my_result))  # Imprime el tipo de dato del valor devuelto (deberia ser int)

def sum(a, b):
    sumo = a + b
    return sumo
result = sum(3, 4)
print("El resultado de la suma es:", result)


def print_name(name, surname, alias = "Sin alias"):

    print(f"{name} {surname} {alias}")

print_name("Juan", "Perez", "JP")  # Llamada a la funcion con alias
print_name("Ana", "Gomez")  # Llamada a la funcion sin alias, usa valor por defecto
print_name(surname="Lopez", name="Carlos")  # Llamada a la funcion con argumentos nombrados

#este asterisco permite recibir varios argumentos como una tupla, 
# si pongo dos asteriscos ** recibe diccionario, si no pongo nada recibe un solo valor
def print_texts(*texto): 

    print(texto)
print_texts("python", "C#", "JavaScript")  # Llamada a la funcion con varios argumentos

def print_texts1(*texto1): 
    print(type(texto1))

    for word in texto1:
        print(word.upper())
    
print_texts1("python", "C#", "Java")  # Llamada a la funcion con varios argumentos







