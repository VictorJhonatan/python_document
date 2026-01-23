### regular expressions - expresiones regulares

"""Ve o verifica que este coincidiendo, 
o busca una coincidencia, o nos puede 
devolver esa coincidencia de esa lista, 
en este caso puede reemplazar un texto

re.match(): busca una coincidencia al inicio de la cadena.

re.search(): busca una coincidencia en toda la cadena.

re.findall(): devuelve todas las coincidencias en una lista.

re.sub(): reemplaza coincidencias por un texto."""
import re #---> (re)regularexpresion - aqui estam todas funciones relacionadas con re

"""Tratan de inspeccionar y cadena de texto """

my_string = "Esta es la lección número 7: expresiones regulares "
my_other_string = "Esta no es la lección número 6: Manejo de ficheros "

# MATCH - buscar una coincidencia en el principio de una cadena de texto, y si no la encuentra, devuelve None.
math = re.match("Esta es la lección", my_string)
math1 = re.match("Esta no es la lección", my_other_string)
print(math.span())  # Resultado: (0, 18) SPA DEVUELVE RESULTADO 0, 18
print(math1.span())  # Resultado: (0, 21) SPA DEVUELVE RESULTADO 0, 21
print()

start, end = math.span()
print(my_string[start: end])
print()

#if math != None: #Otra forma de hacerlo sin usar not
if not(math == None):
    start, end = math.span()
    print(my_string[start: end])
    print()
#otra forma  usando is not
if math1 is not None:
    start, end = math1.span()
    print(my_other_string[start: end])
    print()

print(re.match("Esta es la lección", my_string ))
print(re.match("Esta es la lección", my_other_string))
print()

# search 
string = "Este python: es una leccion y SQL Leccion"

sear = re.search("leccion", string)
print(sear)
start, end = sear.span()
print(string[start: end])
print()

### Findall encuentra todo lo que  tiene leccion

findall = re.findall("leccion", string, re.I) # re.I el "I" busca minuscula y minuscula, tenga tilde o no, igual encuentras
print(findall)
print()

### Split
"""Busca en el string y divide el patron en dos mitad mitad con dos punto :"""
print(re.split(":", string))
print()

### sub ---> sustituye osea lo cambias de minuscula a mayuscula, o al contrario tambien

print(re.sub("python","PYTHON", string))
print(re.sub("Leccion","RegEx", string))
print(re.sub("Leccion|leccion","LECCIÓN", string))
print(re.sub("[l|L]eccion","LECCIÓN", string))
print()

#Crea tu propio patron de expresion regular - ojo mete teoria y practica
"""Analiza patrones . es muy amplio, 
puedes hacer todo tipo de busquedas 
en los string"""

### Patterns
#r es de propio python 
pattern = r"[l|L]eccion"
print(re.findall(pattern, string))

pattern = r"[l|L]eccion|python"
print(re.findall(pattern, string))

pattern = r"[a-z]"
print(re.findall(pattern, string))

pattern = r"[\D]"
print(re.findall(pattern, string))

pattern = r"[l]." #coindicendia con l nada mas
print(re.findall(pattern, string))

pattern = r"[l].*" #coindicendia con l y * y nos da de la L hacia adelante en conjunto
print(re.findall(pattern, string))

#email validation - regular expresion

email = "victordelacruz2412@gmail.com"
pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z-.]+$" #$ el dolar sirve para que siga el string despues del punto
print(re.match(pattern, email))
print(re.search(pattern, email))
print(re.findall(pattern, email))

email = "victordelacruz2412@gmail.e"
print(re.findall(pattern, email))

# https://regex101.com
#Para aprender a validar expresiones regulares

