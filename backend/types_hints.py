### types_hints 

my_variable = "my string variable"  
print(my_variable)
print(type(my_variable))

#cuando cambia la variable de (str) a (int) o cualquiere tipo de dato se llama "tipado dinamico" 
my_variable = 5
print(my_variable)
print(type(my_variable))
print()

my_type_string: str = "my type string variable"
print(my_type_string)
print(type(my_type_string))

my_type_string = 5
print(my_type_string)
print(type(my_type_string))


#QUE ES TIPADO FUERTE --> QUE NO VA PODER CAMBIAR EL VALOR DE LA VARIABÑE SI ES STR SOLO SERA STR NO INT s
"""FastAPI valida los datos que sean correctos,
trabajos en servidor local o podemos crear 
servidor local, cuando este bien va al 
servidor remoto, va por produccion, o cualquier 
entorno que ya se tenga.--------------
SERVIDOR SE LLAMA: uvicorn
este servidor se levanta y se recarga rapido
para hacer un API en nuestra maquina

Conceptos que veremos aqui es:
Backend,,hablar que es API,de todo un CRUD 
de que podemos hacer con un api, como 
autenticar en un API, bases de datos, 
como el backend creando una base de datos 
y almacenar datos y recuperar, borrar, 
todo estos datos se consumen del API"""