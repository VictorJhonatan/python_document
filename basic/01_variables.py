'''
Variables - 
aplicar buena practica - 
usar nombres descriptivos y minusculas con guiones bajos -
Seguir bien la nomenclatura o el tipo de nomenclatura:
LLAMADA_CAMEL_CASE ---> (myvariable) Forma de camello
llamada_Pascal_Case ---> (MyVariable) Forma de pascal
llamada_snake_case ---> (my_variable) Forma de cerpiente
'''
mi_variable = "Soy una variable"
print(mi_variable)

# Algunas Funciones del sistema - usamos len()
print(len(mi_variable))  # Cuenta el numero de caracteres

#Variables int
mi_variable_entero = 10
print(mi_variable_entero)
print("Este es mi numero:", mi_variable_entero)

#Convertir entero a string
mi_variable_string = str(mi_variable_entero)
print(mi_variable_string)
print(type(mi_variable_string))

#Variables booleanas
mi_variable_boolean = False
print(mi_variable_boolean)

# Concatenacion de variables en una sola linea
print(mi_variable, mi_variable_string, mi_variable_boolean)

#variables en una sola linea - no abuses de esta sintaxis
name,  surname, age, is_student = "Victor", "Jhonatan", 21, True
print("Me llamo", name, surname, "mi edad es", age, "años. Estudio:", is_student)

#------------INPUTS------------------
first_name = input("Cual es tu nombre?: ")
age = input("Cual es tu edad?: ")
print("Hola", first_name, "tienes", age, "años.")

#Cambia el valor de las variables
name = "Jose"
age = 30

print(name)
print(age)


