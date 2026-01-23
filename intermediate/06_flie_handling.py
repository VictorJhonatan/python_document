### Manejo de ficheros - file handling

# .txt file
"""parametro "r" modo lectura, 
"w" modo escribir, 
"w+" leer y escribir y sobreescribe 
en el archivo si ya existe (deja vacio) , 
el + es conocido como plus(+)
"r+" solo lee y podemos escribir
"""
import os

txt_file = open("intermediate/my_file.txt", "r+") #leer y escribir
txt_file1 = open("intermediate/my_file2.txt", "w+") #leer y escribir y sobreescribir encima de el
txt_file1.write("Mi Alias es: ArkanoDev\nMi nombre es: Victor Jhona\nMi Apellido es: Rodriguez\nMi edad es: 22 años\nMi lenguaje preferido es: Python\nAunque tambien me gusta SQL")
# print(txt_file.read(10)) #cuenta 10 caracteres
# print(txt_file.read())  #aqui leemos 
# print(txt_file.readline()) # imprime primera linea 
# print(txt_file.readlines()) # imprime todo con lines

for linea in txt_file.readlines(): # lee todas las lineas y lo junta en un listado
    print(linea)
    print()

# escribir con write y se agrega en el archivo my_file.txt
txt_file.write("\nAunque tambien me gusta SQL")

#txt_file1.close()
#os.remove("intermediate/my_file2.txt") #Borra el fichero

print()

### .json file 

"""tipico se usa cuando usas 
aplicaciones web en servidor 
creamos un json, formado clave y valor, 
como diccionario"""

import json # podemos trabajar con json, tiene operaciones

json_file = open("intermediate/my_file.json", "w+") #leer y escribir y sobreescribir

#Pasar un diccionario a fichero Json
json_test = {
    "nombre": "Victor", 
    "apellido": "Rodriguez", 
    "edad": 21,
    "lenguaje": ["Python", "JavaScript"]
    }
#dump escribir el fichero
json.dump(json_test, json_file, indent=4)

# Mover el puntero al inicio del archivo para poder leerlo - seek(0) para que vuelva al principio. ya que usa w+
json_file.seek(0)

data = json.load(json_file)
print(data)
print(type(data))

json_file.close()
print()

# With Abre el archivo en modo lectura - hace que se pueda imprimir
with open("intermediate/my_file.json") as my_other_file:
    for line in my_other_file.readlines():
        print(line)

json_dict = json.load(open("intermediate/my_file.json"))
print(json_dict)
print(type(json_dict))
print(json_dict["nombre"])
print(json_dict.items())
print(json_dict.keys())
print()

# .csv file
import csv

csv_file = open("intermediate/my_file.csv", "w+")
#crear datos csv para que se guarde en el archivo
csv_file = csv.writer(csv_file)
csv_file.writerow(["Name", "surname"])
csv_file.writerow(["Victor", "Rodriguez"])
csv_file.writerow(["Jhona", "Tarzon"])
# csv_file.close # cierra este clse para que puedas ver los datos por pantalla
#para leer debes tener open del archivo

# With Abre el archivo en modo lectura - hace que se pueda imprimir
with open("intermediate/my_file.csv") as my_other_file:
    for line in my_other_file.readlines(): # readlines lee todas las lineas y lo junta en un listado
        print(line)





# .xlsx file
#import xlrd #debe instalarse el modulo

# .xml file
# Abre el archivo en modo escritura
xml_file = open("intermediate/my_file.xml", "w+")

# Escribe el encabezado XML y una estructura básica
xml_file.write('<?xml version="1.0" encoding="UTF-8"?>\n')
xml_file.write('<saludo>\n')
xml_file.write('  <mensaje>Hola</mensaje>\n')
xml_file.write('</saludo>\n')

# Cierra el archivo después de escribir
xml_file.close()

with open("intermediate/my_file.xml") as my_other_file:
    for line in my_other_file.readlines(): # readlines lee todas las lineas y lo junta en un listado
        print(line)







