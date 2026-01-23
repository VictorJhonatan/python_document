### LOOPS - CONOCIDOS COMO BUCLES - TENEMS VARIOS LOOPS ###

### BUCLE WHILE - CLICLO ###
"""
NO TE CONFUNDAS CON EL WHILE TRUE (MIENTRAS SEA VERDADERO HAS ALGO)


EL WHILE HACE QUE EL CODIGO SE REPITA VARIAS VECES E FUNCION O USANDO UA CONDICION ASI COMO SIMILAR A UN IF
"""

my_condition = 0 

while my_condition < 10:
    print(my_condition)
    my_condition += 1  # my_condition = my_condition + 1
else:  # es opcional
    print("Mi condicion es mayor o igual que 10")

print("La ejecucion continua")

my_condition = 0

while my_condition < 20:
    my_condition += 1
    if my_condition == 15:
        print("Se detiene la ejecucion")
        break # termina el ciclo
    print(my_condition)

print()
my_condition = 0
while my_condition < 10:
    print(my_condition)
    my_condition += 2  # my_condition = my_condition + 2

if my_condition == 10: ### ya ssalio del while
    print("Mi condicion es igual a 10")
else: ### ya salio del while
    print("Mi condicion es mayor que 10")


while my_condition < 20:
    my_condition += 2
    if my_condition == 16:
        print("el numero 16 no se muestra")
    print(my_condition)
print("La ejecucion continua")



print()
print("BUCLES FOR")
### BUCLE FOR - PARA CADA ### 
""" 
cumplir la condicion - el FOR sirve para iterar listados de elementos 

EL FOR SE VA REPETIR TANTAS VECES COMO ELEMENTOS QUE TENGAMOS EN LA LISTA O RANGO
"""

list = [35, 24, 62, 52, 12]
for element in list:
    print(element)

print()

my_tuple01 = (19, 20, 21, 22, 23, 24)  # Tupla con elementos
for element in my_tuple01:
    print(element)

print()

my_set3 = {"Victor", "Rodriguez", 21, 22, 23, "Arkano"}  # Set con elementos
for element in my_set3:
    print(element)

print()
dictionary1 = {
    "nombre": "Victor", 
    "apellido": "Rodriguez", 
    "edad": 21,
    }

for element in dictionary1:
    print(element) # imprime las claves del diccionario
    print(dictionary1[element]) # imprime los valores del diccionario
    if element == "apellido":
        print("Se encontro el elemento apellido, saliendo del bucle")
        break ### detiene el for en este punto
        
else: ### este else pertenece al for no al if
    print("Se han terminado los elementos del diccionario")

print("continua la ejecucion") ### este print no pertenece al for
print()

for element in dictionary1:
    print(element) # imprime las claves del diccionario
    if element == "apellido":
        continue ### salta a la siguiente iteracion del for de element
    else:
        print(f"El valor de la clave es: {element}, y su Valor es: {dictionary1[element]}") 
        
else: ### este else pertenece al for no al if
    print("Se han terminado los elementos del diccionario en for")




