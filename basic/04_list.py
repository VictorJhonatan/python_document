### Listas ###
""" Una lista o la palabra lista llamada tambien array o arreglo,
en estructuras de datos con una lista formamos pilas y colas.
Los arreglos no es lo mismo que las listas en python, con un arreglo 
por deninicion tiene menos operaciones que una lista. 

EN LISTAS Y ESTRUCTURAS LA POSICION INICIA EN CERO 0 en todo
"""
print("----Listas-----")

my_list = list()  # Crear una lista vacia
my_list2 = []  # Crear una lista vacia

print(len(my_list))  # Longitud de la lista - 0

my_lists = [19, 20, 21, 22, 23, 24]  # Lista con elementos
print(my_lists)
print(len(my_lists))  # Longitud de la lista - 6

my_listas2 = ["Victor", 21, True, 5.5]  # Lista con diferentes tipos de datos
print(my_listas2)
print(type(my_listas2))  # Tipo de dato - list

print(my_listas2[0])  # Primer elemento - Victor
print(my_lists + [25, 26])  # concatenacion de listas
print(my_lists[-3])  # Tercer elemento desde el final - 22
print(my_lists[-4])  # Cuarto elemento desde el final - 21
print(my_lists[1:4])  # Sublista desde el indice 1 hasta el 3 - [20, 21, 22]
print(my_lists[:3])  # Sublista desde el inicio hasta el indice 2 - [19, 20, 21]
print(my_lists[3:])  # Sublista desde el indice 3 hasta el final
print(my_lists * 2)  # Repeticion de la lista
print(my_lists.count(21))  # Cuenta cuantas veces aparece el elemento 21 - 1
print(my_lists.index(23))  # Indice del elemento 23 - 4

### Modificar listas ###
my_lists.append(27)  # Agrega el elemento 27 al final de la lista
print(my_lists)
print(my_lists.count(27))  # Cuenta cuantas veces aparece el elemento 27 - 1 

my_lists.insert(0, 18)  # Inserta el elemento 18 en la posicion 0
print(my_lists)

""" Modificar un elemento de la lista por su posicion(indice) """
my_lists[0] = "Arkano"  # Modifica el elemento en la posicion 3
print(my_lists)

""" El remove elimina por el valor del elemento(22),"""
my_lists.remove(22)  # Elimina el elemento 22 de la lista
print(my_lists)
print(my_lists.pop(1))  # Elimina el elemento en la posicion 1 y lo devuelve

## Del se elimina por el indice(posicion) ##
del my_lists[2]  # Elimina el elemento en la posicion 2
print(my_lists)

my_new_lists = my_lists.copy()  # Copia la lista

my_lists.clear()  # Limpia la lista
print(my_lists)  # []
print(my_new_lists)  # Muestra la copia de la lista

my_new_lists.reverse()  # Invierte el orden de la lista
print(my_new_lists)

'''my_new_lists.sort()  # Ordena la lista de menor a mayor
print(my_new_lists)'''


### Desempaquetado de listas - cada elemento debe tener su variable sino da ERROR ###
print("----Desempaquetado de listas-----")
name, age, bool, estatura = my_listas2  # Desempaquetado de listas, misma posicion
print(name)  # Victor


###concatenar dos listas ###
print("----Concatenar listas-----") 
list_one = [1, 2, 3]
list_two = [4, 5, "Victor"]
print(list_one + list_two)  # [1, 2, 3, 4, 5, 'Victor']