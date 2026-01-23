# Modulos 

"""
Un modulo es un archivo que contiene codigo de python. 
Este codigo puede definir funciones, clases y variables. 
Tambien puede incluir codigo ejecutable. 
Los modulos permiten organizar y reutilizar el codigo en diferentes partes de un programa o en diferentes programas.

Modulo es una libreria creada por el usuario o por terceros que contiene funciones y clases predefinidas
"""

"""
/Accerde a un modulo(ficheros) usando la palabra reservada import
/Acceder a los datos de modulo ejercicio.py usamos esa palabra reservada import ejercicio. sum es la funcion que queremos usar

import ejercicio  # Importa el modulo ejercicio.py

ejercicio.sum(3, 4)  # definimos los parametros de la funcion (sum) de ejercicio.py

/Aqui llamamos a la función cuart definida en el módulo ejercicio.py

ejercicio.cuart()  # definimos los parametros por un input de la funcion (cuart) de ejercicio.py
---------------------------------------------------------------------------------------------------

/Si quieres importar solo una funcion o clase especifica de un modulo,
puedes usar la palabra reservada from seguida del nombre del modulo y la palabra reservada import
"""

"""el from llama al modulo, el import llama a la funcion o clase especifica del modulo"""

from ejercicio import cuart, sum


sum(5, 7)  # Llama a la función sum del módulo ejercicio.py
cuart()  # Llama a la función cuart del módulo ejercicio.py

# la libreria math es un modulo predefinido de python que contiene funciones y constantes matematicas,
# sirve para hacer operaciones matematicas complejas, como calcular raices cuadradas, logaritmos, funciones trigonométricas, etc.
# tambien sirve para acceder a constantes matematicas como pi y e, entre otras. 
# asi mismo, contiene funciones para redondear numeros, generar numeros aleatorios, y realizar otras operaciones matematicas comunes.

import math  # Importa el módulo math de la biblioteca estándar
math_result = math.sqrt(165)  # Usa la función sqrt del módulo math sirve para calcular la raíz cuadrada
print("La raíz cuadrada de 165 es:", round(math_result, 2))  # Imprime el resultado redondeado a 2 decimales

math.pi_value = math.pi  # Accede a la constante pi del módulo math
print("El valor de pi es:", math.pi_value)
print()
math_log = math.log10(1000)  # Usa la función log10 del módulo math sirve para calcular el logaritmo base 10
print("El logaritmo base 10 de 1000 es:", math_log)

math.pow_result = math.pow(2, 8)  # Usa la función pow del módulo math sirve para calcular potencias
print("2 elevado a la potencia de 8 es:", math.pow_result)

""" la libreria random es un modulo predefinido de python que contiene funciones para generar numeros aleatorios
y realizar selecciones aleatorias. sirve para generar numeros aleatorios enteros o flotantes dentro de un rango especificado
tambien sirve para seleccionar elementos aleatorios de una secuencia como listas, tuplas o cadenas de texto
ademas, contiene funciones para mezclar secuencias y generar muestras aleatorias sin reemplazo
ejemplo: juegos, simulaciones, pruebas tambien se usa en criptografia y seguridad informatica tambien en estadistica y analisis de datos.
en estadistica y analisis de datos te enseña a hacer muestreos aleatorios y simulaciones monte carlo tambien en aprendizaje automatico y ciencia de datos
para dividir conjuntos de datos en conjuntos de entrenamiento y prueba de manera aleatoria. 
sirve para redes neuronales y algoritmos geneticos. 
tambien en pruebas de software para generar datos de prueba aleatorios y escenarios de prueba variados, ayudando a identificar errores y mejorar la robustez del software.
"""

from math import pi as PI_VALUE  # Importa la constante pi del módulo math y la renombra como PI_VALUE
print("El valor de pi importado y renombrado es:", PI_VALUE)
