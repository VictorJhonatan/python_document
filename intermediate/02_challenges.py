### Challanges - Desafíos ###

"""
EL FAMOSO "FIZZ BUZZ”:
Escribe un programa que muestre por consola (con un print) los
números de 1 a 100 (ambos incluidos y con un salto de línea entre
cada impresión), sustituyendo los siguientes:
- Múltiplos de 3 por la palabra "fizz".
- Múltiplos de 5 por la palabra "buzz".
- Múltiplos de 3 y de 5 a la vez por la palabra "fizzbuzz".
"""

def fizzbuzz():
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            print(f"El numero: {i} FizzBuzz")
        elif i % 3 == 0:
            print(f"El numero: {i} Fizz")
        elif i % 5 == 0:
            print(f"El numero: {i} Buzz")
        else:
            print(f"El numero {i} No son multiplos de 3 ni de 5")
fizzbuzz()
print()

"""
¿ES UN ANAGRAMA? -- anagrama es comparar dos palabras si tiene 
las mismas letras, no ver si son iguales las letras Amor - Roma --- 
Amor y roma cumple mismas letras pero en desorden
*** Escribe una función que reciba dos palabras (String) y retorne
verdadero o falso (Bool) según sean o no anagramas.
- Un Anagrama consiste en formar una palabra reordenando TODAS
  las letras de otra palabra inicial.
- NO hace falta comprobar que ambas palabras existan.
- Dos palabras exactamente iguales no son anagrama.
"""
def is_anagrama(word_one, word_two):
    if word_one.lower() == word_two.lower():
        return False
    return sorted(word_one.lower()) == sorted(word_two.lower())

a = is_anagrama("Amor", "Roma")
print(a)
print() 

"""
LA SUCESIÓN DE FIBONACCI
Escribe un programa que imprima los 50 primeros números de la sucesión
de Fibonacci empezando en 0.
- La serie Fibonacci se compone por una sucesión de números en
  la que el siguiente siempre es la suma de los dos anteriores.
  0, 1, 1, 2, 3, 5, 8, 13...
"""

def fibonacci():

    prev = 0
    next = 1

    for _ in range(0, 50): # Usamos un guion bajo para indicar que no necesitamos el índice
        print(prev)
        fib = prev + next
        prev = next
        next = fib

fibonacci()
print()

"""
¿ES UN NÚMERO PRIMO?
Escribe un programa que se encargue de comprobar si un número es o no primo.
Hecho esto, imprime los números primos entre 1 y 100.
"""

def is_primo():
    for number in range(1, 101):

        if number >= 2:
            is_divisible = False
            for index in range(2, number):
                if number % index == 0:
                    is_divisible = True

            if not is_divisible:
                print(number) 
is_primo()
print()

"""
INVIRTIENDO CADENAS
Crea un programa que invierta el orden de una cadena de texto
sin usar funciones propias del lenguaje que lo hagan de forma automática.
- Si le pasamos "Hola mundo" nos retornaría "odnum aloH"
"""
# 1 2 3 4 5 6 7 8 9 10
# 0 1 2 3 4 5 6 7 8 9
# H O L A   M U N D O
def reversa(text):
    text_len = len(text) 
    invertida = ""
    for cadena in range(0, text_len):
        invertida += text[text_len - cadena - 1]
    return invertida
print(reversa("Hola mundo"))

def reversa(text):
    invertida = ""
    for i in range(len(text) - 1, -1, -1):  # Empieza desde el último índice y va hacia atrás
        invertida += text[i]
    return invertida

print(reversa("Hola mundo"))




