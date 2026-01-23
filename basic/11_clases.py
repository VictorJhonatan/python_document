"""
Definición y uso de clases en Python, incluyendo atributos y métodos.
Las clases en Python se definen utilizando la palabra clave 'class', 
seguida del nombre de la clase y dos puntos.

ES IGUAL QUE UNA FUNCION, REALIZA TAREAS, TODO LO QUE ESTA DENTRO DE UNA CLASE RESPONDE A UNA LOGICA ESPECIFICA
ejmeplo: la clase persona debe tener logica relaciona con una persona: nombre, apellido, edad, hablar, caminar, etc

"""
class MyPersona: ###uso pascal case para las clases
    pass ###uso pass para indicar que la clase esta vacia

class Persona:
    """Las clases tienen constructores."""
    def __init__(self, name, surname, age):
        self.nombre = name  # Atributo de instancia ---> .nombre es el atributo(propiedad) de la clase = name que es el parametro
        self.apellido = surname  # Atributo de instancia
        self.edad = age  # Atributo de instancia

#creo una variable
my_person = Persona("Victor", "Jhonatan", 21)  # Creo una instancia de la clase Persona
print(f"Mi Nombre es: {my_person.nombre}, y mi Apellido es: {my_person.apellido},  la Edad que tengo es: {my_person.edad}")  # Accedo a los atributos de la instancia
print()

print("-----SEGUNDO EJEMPLO DE CLASES-----")
class person1:
    def __init__(self):
        self.name = "Victor"
        self.surname = "Romero"
        self.age = "17"
my_person1 = person1()
print(f"Mi Nombre es: {my_person1.name}, y mi Apellido es: {my_person1.surname},  la Edad que tengo es: {my_person1.age}")

print()
print("-----TERCER EJEMPLO DE CLASES CON METODOS-----")

class Person2:
    def __init__(self, name, surname, alias="Sin alias"):
        self.full_name = f"{name} {surname} ({alias})"  # Atributo de instancia - self. es publico
        self.__nombre = name  # Atributo de instancia - self. es privado (propiedad privada)


    # creamos una funcion dentro de la clase, se llama metodo
    def walk(self):
        print(f"{self.full_name} esta caminando")  # Metodo de instancia

    def get_name(self):
        return self.__nombre  # Metodo para acceder al atributo privado

    def talk(self):
        print(f"{self.full_name} esta hablando")  # Metodo de instancia

my_person2 = Person2("Victor", "Romero")

print("Mi nombre completo es:", my_person2.full_name)  # Accedo al atributo de la instancia
print("Mi nombre privado es:", my_person2.get_name())  # Accedo al atributo privado de la instancia

my_person2.walk()  # Llamo al metodo de la instancia

print()

my_person3 = Person2("Ana", "Gomez", "AG")  # Creo otra instancia de la clase Person2

print("Mi nombre completo es:", my_person3.full_name)  # Accedo al atributo

my_person3.talk()  # Llamo al metodo de la instancia

# Modifico el atributo de la instancia
my_person3.full_name = "Victor De La Cruz - (ArkanoDev)"  # Modifico el atributo de la instancia
print("Mi nuevo nombre completo es:", my_person3.full_name)  # Accedo al

print(type(my_person3.full_name))  # Imprime el tipo de dato de la instancia (deberia ser <class '__main__.Person2'>)



