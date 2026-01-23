"""
Set: Conjunto de elementos únicos y desordenados. A diferencia de las listas y tuplas, 
los sets no permiten elementos duplicados.
Se definen con llaves {} o con la función set().

U set no es una estructura ordenada, no tiene indice, no se puede acceder a sus elementos por posicion.

"""

my_set = set()  # Crear un set vacío usando el constructor set()
my_set2 = {}  # Crear un set vacío usando llaves (esto en realidad crea un diccionario vacío)

print(type(my_set))  # Tipo de dato 

my_set3 = {"Victor", "Rodriguez", 21, 22, 23, "Arkano"}  # Set con elementos
print(my_set3)
print(type(my_set3))  # Tipo de dato - set

"""operaciones con sets"""

print(len(my_set3))  # Longitud del set - 6

my_set3.add("2003")  # Agregar un elemento al set, el set no es una estructura ordenada
print(my_set3)

my_set3.add("2003")  # Set no permite elementos duplicados
print(my_set3)

"""El set es como un hash interno """
my_set3.remove(21)  # Elimina el elemento 21 del set
print(my_set3)
my_set3.discard(30)  # Elimina el elemento 30 del set si existe, no da error si no existe
print(my_set3)
my_set3.pop()  # Elimina un elemento aleatorio del set
print(my_set3)

"""comprobar si un elemento existe en el set"""
print("Victor" in my_set3)  # True
print("21" in my_set3)  # False

"""Operaciones
my_set3.remove("Arkano")  # Elimina el elemento "Arkano" del set
print(my_set3)"""

my_set3.update(["Python", "Java", "C++"])  # Agrega varios elementos al set
print(my_set3) # 

my_set3.discard("Rodriguez")  # Elimina el elemento "Rodriguez" del set si existe
print(my_set3)

"""Del palabra reservada del sistema"""
#del my_set3  # Elimina el set completo


"""Convertir set a lista para poder modificarlo  PERO OJO ES MALA TECNICA"""
my_set4 = {"Python", "Java", "C++"}
my_list = list(my_set4)  # Convertir set a lista
print(my_list)
print(type(my_list))  # Tipo de dato - list
print(my_list[0:2]) 
my_list[0] = "JavaScript"  # Modificar el primer elemento de la lista
print(my_list)

my_set5 = {"linux", "windows", "macOS"}

my_new_set = my_set4.union(my_set5)  # Union de dos sets
print(my_new_set)
print(my_new_set.union(my_new_set).union(my_set3).union({"Juan"}))  # Union de varios sets, pero no acepta repeticiones

