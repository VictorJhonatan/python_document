"""
Docstring for 08_conditionals 
Las condiciones son es: Se se cumple ua condicion se ejecuta un bloque de codigo, 
si no se cumple se ejecuta otro bloque de codigo diferente.
"""

my_condition = False

if my_condition:  # es los mismo ---- if my_condition == True:
    print("Se ejecuta la condicion del IF")  # Bloque de codigo si la condicion es verdadera

my_condition = 5 * 3

if my_condition == 10: 
    print("Se ejecuta la segunda condicion del IF") 

if my_condition > 16 and my_condition < 20: 
    print("Es mayor que 10 y menor que 20") 
elif my_condition == 15:
    print("Es igual a 15")
else:
    print("Es menor o igual que 10 o mayor o igual que 20") 

print("La ejecucion continua") # fuera del if


my_string = "Hola"

if my_string:  # evalua si la cadena no esta vacia
    print("La cadena no esta vacia")



