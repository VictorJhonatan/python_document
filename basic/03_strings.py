### String ### Manipulacion de cadenas ###
print("----String Manipulacion de cadenas-----")

my_string = "Hola, Victor!" ## Doble comillas
my_string2 = 'Python es genial.' ## Comillas simples

print(len(my_string))  # Longitud de la cadena

print(my_string[0])    # Primer caracter

print(my_string + " No crees que " + my_string2)  # Concatenacion de cadenas

my_new_line_string = "Hola,\nVictor!"  # Nueva linea con \n ---> salto de linea
print(my_new_line_string)

my_tab_string = "Hola,\t Victor!"  # Tabulacion con \t ---> espacio tabulado
print(my_tab_string)

my_scape_string = "\t Hola, Victor! \nComo estas" 
print(my_scape_string)

my_scape_string = "\\t Hola, Victor! \\nComo estas" ## Escapando caracteres

"""Se crear scripts con python para monitorear cambios en una web, SI SE PUEDE,
python es para crear scripts, automatizar tareas, crear aplicaciones web,
crear aplicaciones de escritorio, crear juegos, crear aplicaciones de inteligencia artificial"""


### Formateos ### se usa para formatear e imprimir cadenas de texto mas rapido ###
print("----Formateos . cademas de texto - PRINT-----")
name = "Victor"
surname = "Jhonatan"
age = 21
#### %s es para cadenas, %d es para enteros --- % formateas
print("Mi nombre es %s %s y tengo %s años.". format(name, surname, age)) #da error si usas %s con .format
###---------------------------------------------------------------------------
### para usar .format() no uses %s usa {} como marcador de posicion
###Usamos llaves {} si queremos que imprima ese dato
###Usamos %s o %d %f si usamos el formateo es mejor ya que imprime mucho mejor los datos
print("Mi nombre es {} {} y tengo {} años.". format(name, surname, age))
print("Mi nombre es %s %s y tengo %d años." % (name, surname, age))  # Formateo con %
print(f"Mi nombre es {name} {surname} y tengo {age} años." ) # Formateo con f Imprime mas rapido y facil

"""
Esto es tipico ya que nos sirve cuando  Internacionalizamos textos,
si tuvieras una apliacion en español, ingles y nos va poner en idioma que pongamos"""

###Desempaquetado de cadenas(caracteres) ###
print("---Desempaquetado de cadenas---")

language = "python"
a, b, c, d, e, f = language  # Desempaquetado
print(a)  # P
print(b)  # y
print(c)  # t
print(d)  # h
print(e)  # o
print(f)  # n

### Division de cadenas ###
print("----Division de cadenas-----")
language_slide = language[0:5]  # Primeros tres caracteres
print(language_slide)  # pytho

language_slide = language[1:]  # Primer 1 caracter hasta el final
print(language_slide) ### ython

language_slide = language[-6:-1]  # Ultimos 5 caracteres menos el ultimo
print(language_slide) ### pytho


### Reverse string - Cadena invertida ###
print("----Reverse string - Cadena invertida-----")
language_reverse = language[::-1]  # Cadena invertida - python
print(language_reverse)  # nohtyP 

####Funciones de cadenas ###
print("----Funciones de cadenas-----")
print(language.capitalize())  # Primera letra en mayuscula
print(language.upper())  # Todo en mayusculas
print(language.lower())  # Todo en minusculas  
print(language.count("t"))  # Cuenta cuantas veces aparece un caracter
print(language.isnumeric())  # Comprueba si es numerico
print("1".isnumeric())  # Comprueba si es numerico
print(language.isalpha())  # Comprueba si es alfabetico
print(language.upper().isupper()) ## concatenacion de funciones .isupper()-->Comprueba si es mayuscula
print(language.startswith("py"))  # Comprueba si empieza con py