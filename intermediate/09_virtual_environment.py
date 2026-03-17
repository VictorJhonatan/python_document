### virtual environment - entorn virtual
""" Es un entorno  virtual que permite 
tener un espacio aislado para instalar 
paquetes y dependencias de Python sin 
afectar el sistema global. 
Esto es especialmente útil cuando se 
trabaja en múltiples proyectos que 
pueden requerir diferentes versiones de paquetes.
Para crear y gestionar entornos virtuales 
en Python, se puede utilizar el módulo incorporado `"""

#### Comando:--> |-------------python -m venv venv
""" Python:
le estás diciendo a la terminal 
que use Python para ejecutar un módulo o comando.
Si tu sistema tiene múltiples versiones de Python 
instaladas (por ejemplo, Python 2 y Python 3), 
puedes necesitar usar python3 en lugar de python."""

""" -m:
Esta opción le dice a Python que ejecute 
un módulo como un script. Los módulos son 
pequeños programas o bibliotecas que 
Python puede ejecutar.
En este caso, estamos diciendo a Python 
que ejecute el módulo venv."""

"""venv:
Es el módulo de Python que se utiliza 
para crear y gestionar entornos virtuales.
Este módulo permite crear un directorio 
aislado (el entorno virtual) donde se pueden 
instalar dependencias sin interferir con las 
librerías globales de Python."""

""" venv (última palabra en el comando):
Este es el nombre de la carpeta donde 
se creará el entorno virtual.
Puedes darle cualquier nombre a esta 
carpeta, pero por convención, suele 
llamarse venv o env. Es"""

###DESPUES DE ESO ACTIVAR EL ENTORNO VIRTUAL
""" Una vez creado el entorno virtual, 
debes activarlo para empezar a usarlo.
- En Windows:
  ```bash
  .\venv\Scripts\activate
  .venv\Scripts\activate (para entornos virtuales creados con el nombre .venv)
  ```"""

""" ¿Qué sucede si no activas el entorno virtual?
Si no activas el entorno virtual y tratas de 
ejecutar tu proyecto o instalar librerías, 
el sistema usará las librerías globales de Python, 
lo cual no es lo que deseas, ya que puede haber 
conflictos de versiones entre proyectos o 
dependencias."""

### COMANDO FINAL |---- deactivate
