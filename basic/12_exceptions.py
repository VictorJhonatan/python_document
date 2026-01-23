### Exceptiones in Python

"""Las excepciones en Python son eventos que ocurren durante la ejecución de un programa,
Excepciones son para controlar errores y manejar situaciones inesperadas sin que el programa se detenga abruptamente.
permitiendo que el programa continúe su ejecución o maneje el error de manera adecuada.
Se manejan utilizando bloques try y except."""

print("-----EJEMPLO DE EXCEPCIONES - EXECEPCIONES POR TIPO-----")

def divide_numbers(num1, num2):
    ###si queremos controlar errorres usamos el bloque try except
    try: # intento ejecutar este codigo
        result = num1 / num2
    except ZeroDivisionError: # si ocurre este error hago esto
        return "Error: No se puede dividir por cero."
    except TypeError: # se ejecuta si ocurre este error osea si el tipo de dato es incorrecto
        return "Error: Ambos argumentos deben ser números."
    else: # si no ocurre ningun error hago esto
        return f"El resultado de la división es: {result}"
    finally:
        print("Ejecución del bloque finally.")

return_value = divide_numbers(10, 2)
return_value1 = divide_numbers(10, 0)
return_value2 = divide_numbers(10, "a")
print(return_value)  # Imprime el resultado de la división
print(return_value1)  # Imprime el resultado de la división por cero
print(return_value2)  # Imprime el resultado de la división con tipo de dato incorrecto


print()
print("-----SEGUNDO EJEMPLO DE EXCEPCIONES-----")

num = 1
num2 = 4
num2 = "4"

try:
    div = num < num2
    print(f"{div}")
    
except:
    print("Ha ocurrido un error en la división.")

else: # si no ocurre ningun error hago esto
    print(f"no hay errores")

finally: # se ejecuta siempre
    print("La ejecución continua.")

print()
print("-----EXECEPCIONES POR TIPO-----")

num5 = 1
num6 = "4"

try:
    div = num5 < num6
    print(f"{div}")

except ValueError:
    print("Ha ocurrido un value error.")
    
except TypeError: # se ejecuta si ocurre este error osea si el tipo de dato es incorrecto
    print("Ha ocurrido un error en type error.")


else: # si no ocurre ningun error hago esto
    print(f"no hay errores")

finally: # se ejecuta siempre
    print("La ejecución continua.")


print()
num8 = 5
num9 = "2"

try:
    div = num8 / num9
    print(f"{div}")

except ValueError as error: # dentro de error se almacena ese error de la eceion value
    print(error)
except Exception as error: # se ejecuta si ocurre este error osea si el tipo de dato es incorrecto
    print(f"Error de tipo: {error}")

else: # si no ocurre ningun error hago esto
    print(f"no hay errores")

finally: # se ejecuta siempre
    print("La ejecución continua.")
