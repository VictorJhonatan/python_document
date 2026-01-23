class MyClass:
  x = 5

print(MyClass)

#c Crea un objeto llamado p1 e imprime el valor de x:
p1 = MyClass()
print(p1.x)

# Accede a las propiedades de un objeto:
class Car:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

car1 = Car("Toyota", "Corolla")

print(car1.brand)
print(car1.model)
print()

# MODIFICAR ( Cambiar la propiedad de edad:)
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("Tobias", 25)
print(p1.age)

p1.age = 26
print(p1.age)