def sum(a, b):
    
    print(a + b)


# ejercicio.py --- pasar a modulo 13_modules.py ---
"""Primera forma -----------------------------------------------------------------------------
def tree():

    number = int(input("Ingresa un número para saber si es par o impar: "))
    if number % 2 == 0:
        print(f"El número {number} es par.")
    else:
        print(f"El número {number} es impar.")
    
    continuar = input("¿Deseas ingresar otro número? (s/n): ").lower()

    while continuar != 's':
        break
    else:
        number = int(input("Ingresa un número para saber si es par o impar: "))
        continuar = input("¿Deseas ingresar otro número? (s/n): ").lower()
"""

def cuart():
    while True:
        number = int(input("Ingresa un número para saber si es par o impar: "))
        if number % 2 == 0:
            print(f"El número {number} es par.")
        else:
            print(f"El número {number} es impar.")
        
        continuar = input("¿Deseas ingresar otro número? (s/n): ").lower()
        if continuar != 's':
            print("Programa finalizado.")
            break  
    

# primera forma------------------------------------------------------------------------------
"""
def one(numero):
    if numero % 2 == 0:
        print(f"El numero {numero} es par")
    else:
        print(f"El numero {numero} es impar")
    return

result = one(int(input("ingrese un numero para saber si es par o impar: ")))
continue_prompt = input("¿Desea ingresar otro numero? (s/n): ")

while continue_prompt.lower() != 's':
    break
else:
    result = one(int(input("ingrese un numero para saber si es par o impar: ")))
    continue_prompt = input("¿Desea ingresar otro numero? (s/n): ")

"""

#SEGUNDA FORMA-----------------------------------------------------------------------
"""
def two(num):
    if num % 2 == 0:
        print(f"El numero {num} es par")
    else:
        print(f"El numero {num} es impar")
    return

while True:
    number = int(input("ingrese un numero para saber si es par o impar: "))
    result = two(number)
    continue_prompt = input("¿Desea ingresar otro numero? (s/n): ")
    if continue_prompt.lower() != 's':
        break
"""




    

    