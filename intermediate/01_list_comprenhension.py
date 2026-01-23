### List Comprehensions - Listas por comprensión ###

list_original = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9 , 10]
list_nueva = [i for i in range(11)]
print(list_nueva)

my_rango = list(range(11))
print(my_rango)

my_list = [i + 1 for i in range(8)]
print(my_list)

my_list = [i * 1 for i in range(8)]
print(my_list)

my_list = [i * i for i in range(8)]
print(my_list)

def sum_five(number):
    return number + 5

my_list = [sum_five(i) for i in range(8)]
print(my_list)