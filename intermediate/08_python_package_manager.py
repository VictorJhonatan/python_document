### Python Package Manager - Administrador de paquetes de Python ### 

"""Es un gestor de paquetes para python, 
osea que si queremos utilizar un modulo 
que no tengamos descargado, debemos usar esto"""

# PIP
"""Asi mismo desde consola podemos
manejar nuestro gestor aparte de 
descargar dependencias, podremos 
manejar versiones de python"""
 # PIP --version
 # PIP install
 #pip muestra que puedes hacer con ello

import numpy # pip install numpy

print(numpy.version.version)

numpy_array = numpy.array([19, 20, 21, 22, 23, 24])
print(type(numpy_array))
print(numpy_array * 2)
print()

import pandas # pip install pandas
# "pip list - permite ver los paquetes(librerias cargadas y las instaladas)" 
# pip unistall pandas
# pip show numby - muestra la informacion de toda la libreria
import requests # es hacer peticiones al API


# Arithmetics Package
from mypackage import arithmetics
print(arithmetics.sum(3, 5))