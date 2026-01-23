### error types - tipos de error ###

"""Como buenos programadores debemos usar 
excepciones para poder capturar errores, 
y no provovarlo, y el porque se dan 
estos errores - Vamos a repasar excepciones """

###syntaxError
print("Hola, que tal")
print()
### nameError ###
lenguaje = "Spanish" ### comenta esta linea para ver el error
print(lenguaje)
print()
### IndexError ###
my_list = ["python", "C#", "Java", "Dark"]
print(my_list[0: 2])
print(my_list[-2])
print(my_list[3])
#print(my_list[4]) # da error, indice 4 ya no existe, siempre empieza desde 0(indice)
print()

### ModuleNotFoundError
#import maths ---> Descomenta y te sale el error
import math

### AttributeError
#print(math.PI) # descomenta esto y sale el error, no existe el atributo
print(math.pi)
print()

###KeyError

dictionary1 = {
    "nombre": "Victor", 
    "apellido": "Rodriguez", 
    "edad": 21,
    }

print(dictionary1["edad"]) # manera correcta
# print(dictionary1["edad1"])   #error clave(key) edad1
# print(list["nombre"])    #error typeError

### TypeError

# print(list["Nombre"]) # typeError ---- comentado

print(list["0"]) #type error - es str
print(list[0]) # int
print(list[False]) # bool
print()

### importError
# from math import PI #importError de PI no existe no hay - descomenta

from math import pi as valor_pi

x = valor_pi * 10
print(valor_pi)
print(x)
print()

### ValueError

my_int = int("10")
# my_int1 = int("10 años")
print(type(my_int))
print(my_int * 2 )
# print(type(my_int1)) ## Value Error - descomentar


###ZeroDivisiónError

print(5 / 2)
# sprint(5 / 0) # ZeroDivisiónError - decomentar





