### Lambdas en python ###
"""
Es como funciones - 
Lambdas hace funciones anominas, 
osea funciones que no tienen nombre
Palabra reservada lambda, este puede 
tener parametros de entrada
"""

sum_two_value = lambda first_value, second_value: first_value + second_value
print(sum_two_value(2, 4))
print()
multiply_value = lambda first_value, second_value: first_value * second_value + 4
print(multiply_value(2, 4))
print()

def sum_value(value):
    return lambda first_value, second_value: first_value * second_value + value

my_sum = sum_value(8)(5, 2)
print(my_sum)

