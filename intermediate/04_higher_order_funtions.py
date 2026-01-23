### Higher_order_funtions- funciones de orden superior ### 

"""
Son funciones que hacen consas 
con funciones dentro de otras funciones,
Definir funciones dentro de otras para 
asi poder operar con ellas, y tambien 
con funciones del sistema del mismo lenguaje """

from functools import reduce

def sum_one(value):
    return value + 1

def sum_value_and_one(first_value, second_value):
    return sum_one(first_value + second_value)

sum = sum_value_and_one(5, 2)
print(sum)
print()

def sum_two(values):
    return values + 5

def sum_two1(values1):
    return values1 + 10

def sum_add_two(num1, num2, f_sum):
    return f_sum(num1 + num2)

sum1 = sum_add_two(5, 2, sum_two)
sum2 = sum_add_two(5, 2, sum_two1)
print(sum1)
print(sum2)
print()

### Closures ###

"""
Hace referencia a las funciones  de orden superior """

def sum_ten(original):
    def add(value):
        return value + 10 + original
    return add
    
add_closure = sum_ten(2)
add = add_closure(5)
print(add) # 17

add2 = sum_ten(5)(4)
print(add2) # 19

add3 = (sum_ten(5))(5)
print(add3) # 20
print()

### Higher_order_funtions ###
### funciones de orden superior, incorporadas del sistema ###

# map ITERA CADA VALOR DE MI LISTA
"""Recorre todos los valores y ejecuta la funcion con cada uno de ellos, para modificar su valor"""
number = [1, 2, 3, 4, 20, 30]
def multiply_two(num):
    return num * 2

x = list(map(multiply_two, number))
print(x)

y = list(map(lambda num1: num1 * 2, number))
print(y) 

### filter ### define una funtion para que te de true o false--- para saber como filtrar
"""Recorre todos sus valores y ejecuta una funcion que retorna  true o false para saber como filtrar"""
def filters_one(number):
    if number > 10:
        return True
    return False

s = list(filter(filters_one, number))
print(s)

lam = list(filter(lambda number: number > 10, number))
print(lam)
print()

### funtions Reduce
# 1, 2, 3, 4, 20, 30
def sum_t(first_value, segun_value):
    #print(first_value)
    #print(segun_value)
    return first_value + segun_value
print(reduce(sum_t, number))

