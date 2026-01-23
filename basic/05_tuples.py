""" Tuplas: Son inmutables, 
no se pueden modificar una vez creadas. 
Se definen con parentesis () """

print("----Tuplas-----")
my_tuple = tuple()  # Crear una tupla vacia - tuple() es el constructor para crear tuplas
my_tuple2 = ()  # Crear una tupla vacia 

my_tuple01 = (19, 20, 21, 22, 23, 24)  # Tupla con elementos
print(my_tuple01)
print(type(my_tuple01))  # Tipo de dato - tuple
print(len(my_tuple01))  # Longitud de la tupla - 6
print(my_tuple01[0])  # Primer elemento - 19
print(my_tuple01[-1])  # Ultimo elemento - 24
print(my_tuple01[1:4])  # Subtupla desde el indice 1 hasta el 3 - (20, 21, 22)

""" La tupla es lo mismo que una lista pero inmutable, no se puede modificar, 
agregar, eliminar elementos una vez creada la tupla
en algunos lenguajes de programacion  hay como especificaciones
en alguno conceptos le dicen duplas(hay 2 elementos) tripletas, tripla(3 elementos)
o cuartetas, cuadrupla(4 elementos)"""

print(my_tuple01 + (25, 26))  # Concatenacion de tuplas
print(my_tuple01 * 2)  # Repeticion de la tupla
print(my_tuple01.count(21))  # Cuenta cuantas veces aparece el elemento 21 - 1
print(my_tuple01.index(23))  # Indice del elemento 23 - 4
print(my_tuple01 + (27, 28, 29))  # Concatenacion de tuplas

print("---Desempaquetado de tuplas-----")
### Desempaquetado de tuplas - cada elemento debe tener su variable sino da ERROR
a, b, c, d, e, f = my_tuple01
print(a)  # 19

"""Convertir la tupla en lista para poder modificarla"""
my_tuple_to_list = list(my_tuple01)  # Convertir tupla a lista
print(type(my_tuple_to_list))  # Tipo de dato - list

my_tuple_to_list[2] = 99  # Agregar el tercer elemento de la lista
print(my_tuple_to_list)  # Mostrar la lista 

my_tuple_to_list.insert(1, 15)  # Insertar un elemento en la posicion 1
print(my_tuple_to_list)  # Mostrar la lista

my_tuple02 = tuple(my_tuple_to_list)  # Convertir lista a tupla
print(type(my_tuple02))  # Tipo de dato - tuple


