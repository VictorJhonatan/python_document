### Encapsulation - encapsulamiento de clases 

# Propiedades privadas
"""
class Person:
  def __init__(self, name, age):
    self.name = name
    self.__age = age # Private property

p1 = Person("Emil", 25)
print(p1.name)
print(p1.__age) # This will cause an error
"""

# Para acceder a una propiedad privada, puede crear un método getter:
class Person:
  def __init__(self, name, age):
    self.name = name
    self.__age = age

  def get_age(self):
    return self.__age

p1 = Person("Tobias", 25)
print(p1.get_age())
print()

"""Establecer el valor de la propiedad privada
Para modificar una propiedad privada, puede 
crear un método setter.Utilice un método 
setter para cambiar una propiedad privada:"""

class Person:
  def __init__(self, name, age):
    self.name = name
    self.__age = age

  def get_age(self):
    return self.__age

  def set_age(self, age):
    if age > 0:
      self.__age = age
    else:
      print("Age must be positive")

p1 = Person("Tobias", 25)
print(p1.get_age())

p1.set_age(26)
print(p1.get_age())
print()

# ¿Por qué utilizar la encapsulación?
"""
La encapsulación proporciona varios beneficios:

Protecția datelor: Previene la modificación accidental de datos
Validación: Puede validar los datos antes de configurarlos
Flexibilidad: La implementación interna puede cambiar sin afectar el código externo
Control: Tiene control total sobre cómo se accede y modifica a los datos"""

class Student:
  def __init__(self, name):
    self.name = name
    self.__grade = 0

  def set_grade(self, grade):
    if 0 <= grade <= 100:
      self.__grade = grade
    else:
      print("Grade must be between 0 and 100")

  def get_grade(self):
    return self.__grade

  def get_status(self):
    if self.__grade >= 60:
      return "Passed"
    else:
      return "Failed"

student = Student("Emil")
student.set_grade(85)
print(student.get_grade())
print(student.get_status())
print()

"""Propiedades protegidas
Python también tiene una convención 
para propiedades protegidas que 
utilizan un solo guión bajo _ prefijo:"""

class Person:
  def __init__(self, name, salary):
    self.name = name
    self._salary = salary # Protected property

p1 = Person("Linus", 50000)
print(p1.name)
print(p1._salary) # Can access, but shouldn't