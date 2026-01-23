### Operadores Aritmeticos ###
print("----Operadores Aritmeticos-----")
print(5 + 3)  # Suma
print(5 - 3)  # Resta
print(5 * 3)  # Multiplicacion  
print(5 / 3)  # Division
print(5 // 3) # Division entera
print(5 % 3)  # Modulo (residuo de la division)
print(5 ** 3) # Exponente (5 elevado a la 3)
print(10 ** 2 + 5 - 4 / 2) # Operaciones combinadas

print("Hola Victor " + "Jhonatan") # Concatenacion de cadenas
print("Hola " + str(5)) # Concatenacion de cadena con numero convertido a cadena
print("Hola " * 3) # Repeticion de cadenas
print("Hola " * (2 + 1)) # Repeticion con operacion
print("Hola " * (2 ** 3)) # Repeticion con operacion

my_float = 5.5 * 2 #11.0
print("Hola " * int(my_float)) # Repeticion con numero float convertido a entero #11


### Operadores de Comparacion ###
print("----Operadores Comparacion-----")
print(5 > 3)   # Mayor que
print(5 < 3)   # Menor que
print(5 >= 3)  # Mayor o igual que
print(5 <= 3)  # Menor o igual que
print(5 == 3)  # Igual que
print(5 != 3)  # Diferente que
print("Hola" == "Hola")  # Igual que cadenas
print("Hola" != "Python")  # Diferente que cadenas
print(5 > 3 + 1)  # Operacion en comparacion
print(5 == 2 * 2 + 1)  # Operacion en comparacion

print("Hola" > "Python")  # Comparacion alfabetica - H es mayor que P --- POR ASCII
print("Hola" < "Python")  # Comparacion alfabetica - H es menor que P
print(len("Hola") > len("Python"))  # Comparacion de longitud de cadenas - cuent cada una

print()
### Operadores Logicos ### Aprende logica booleana - tabla de verdad ### conjuncion , disyuncion, negacion ###
print("----Operadores Logicos-----")
print(True and False)  # AND - Y
print(True or False)   # OR - O
print(not True)        # NOT - NO
print(not False)       # NOT - YES
print((5 > 3) and (10 < 5))  # Operaciones combinadas con AND
print((5 > 3) or (10 < 5))   # Operaciones combinadas con OR
print(not (5 > 3))           # Operacion combinada con NOT
print((5 > 3) and not (10 < 5))  # Operacion combinada AND y NOT

number = 10
number2 = 5
suma = number + number2
print("La suma es:", suma)
es_mayor = suma > 10 and not(suma < 20)
print("Es: ", es_mayor)

