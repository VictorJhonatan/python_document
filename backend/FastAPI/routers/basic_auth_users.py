from fastapi import Depends, FastAPI, HTTPException, status
from pydantic import BaseModel
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

"""OAuth2PasswordBearer es una 
clase de FastAPI que nos permite 
implementar la autenticación como 
usuario y contraseña utilizando 
el protocolo OAuth2.

---> OAuth2PasswordRequestForm es 
la forma en la que se envían los 
datos de autenticación, es decir, 
el nombre de usuario y la contraseña. 
Osea backend captura el nombre de 
usuario y la contraseña que el cliente 
envía a través de un formulario, 
y luego utiliza esos datos para 
autenticar si el usuario es válido o no.
"""
app = FastAPI()

#creamos un router para los usuarios, que es el que vamos a utilizar para la autenticación, y lo incluimos en el main.py para que esté disponible en toda la aplicación.
oauth2 = OAuth2PasswordBearer(tokenUrl="login")

class User(BaseModel):
    username: str
    full_name : str
    email: str
    disabled: bool # esta vatriable si esta habilitado o deshabilitado el usuario

"""Esta clase UserInDB hereda de la clase User, 
lo que significa que tiene todos los atributos 
de la clase User, pero además tiene un atributo 
adicional llamado password, que es la contraseña
 del usuario. Esta clase se utiliza para representar 
 a un usuario en la base de datos, ya que en la base 
 de datos se almacena la contraseña del usuario, 
 mientras que en la clase User no se almacena la 
 contraseña por razones de seguridad."""

class UserInDB(User):
    password: str

#estamos creando una bd de usurios, de formato diccionario, donde la clave es el nombre  de usuario y el valor es otro diccionario con la información del usuario
user_db = {

    "victor": {
        "username": "victor",
        "full_name": "Victor Robles",
        "email": "victor@victor.com",
        "disabled": False,
        "password": "123456"
    },

    "analu": {
        "username": "ana",
        "full_name": "Ana García",
        "email": "ana@ana.com",
        "disabled": True,
        "password": "123456"
    },

    "luis": {
        "username": "luis",
        "full_name": "Luis Martínez",
        "email": "luis@luis.com",
        "disabled": False,
        "password": "123456"
    }
}

#fun sin la contraseña, entrega todos los datos del usurio pero sin su contraseña
def search_users(username: str):
    if username in user_db:
        return User(**user_db[username])

def search_user(username: str):
    if username in user_db:
        return UserInDB(**user_db[username]) # **user_db[username] es una forma de desempaquetar el diccionario que se encuentra en user_db[username], lo que significa que se están pasando los valores del diccionario como argumentos a la clase UserInDB para crear una instancia de esa clase con esos valores. Por ejemplo, si username es "victor", entonces user_db[username] es el diccionario {"username": "victor", "full_name": "Victor Robles", "email": "


"""esta funccion es un criterio de 
dependencia, es decir, es una función 
que se utiliza para verificar si el 
usuario que está intentando acceder a 
una ruta privada está autenticado y 
tiene permisos para acceder a esa ruta. 
Esta función se utiliza como una dependencia 
en las rutas privadas, lo que significa que 
antes de ejecutar la ruta privada, se ejecuta 
esta función para verificar si el usuario está 
autenticado y tiene permisos para acceder a esa ruta. 
Si el usuario no está autenticado o no tiene permisos 
para acceder a esa ruta, se devuelve un error de autenticación o autorización.

headers={"WWW-Authenticate": "Bearer"} es un encabezado 
que se utiliza para indicar que la autenticación se 
realiza utilizando el protocolo Bearer, lo que significa 
que el token de acceso se envía en el encabezado de la 
solicitud utilizando el formato "Bearer <token>". 
Este encabezado se utiliza en la función current_user 
para indicar que la autenticación se realiza utilizando 
el protocolo Bearer, lo que significa que el token de 
acceso se envía en el encabezado de la solicitud utilizando 
el formato "Bearer <token>". Si el token de acceso no es válido, 
se devuelve un error de autenticación con este encabezado para 
indicar al cliente que debe enviar un token de acceso válido para acceder a la ruta privada.
"""  
async def current_user(token: str = Depends(oauth2)):
    user = search_users(token)
    if not user:  # if user is None
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, 
            detail="credenciales  de autenticación inválidas", 
            headers={"WWW-Authenticate": "Bearer"})
    
    if user.disabled:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Usuario inactivo")
    return user
    
@app.post("/login")
async def login(form: OAuth2PasswordRequestForm = Depends()):
    users_db = user_db.get(form.username)
    if not users_db:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="El usuario no es correcto")
    
    user = search_user(form.username)
    if not form.password == user.password: # si la contraseña no es correcta
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Contraseña incorrecta")
    
    return {"access_token": user.username, "token_type": "bearer"}

"""Cuando un se autentica correctamente, 
se devuelve un token de acceso(access_token), 
que en este caso es el nombre de usuario del
usuario autenticado. Este token se utiliza 
para acceder a las rutas privadas de la API, 
es decir, las rutas que requieren autenticación. 
Para acceder a estas rutas, el cliente debe enviar 
el token de acceso en el encabezado de la solicitud, 
utilizando el formato "Bearer <token>".
El servidor luego verifica el token y si es válido, 
permite el acceso a la ruta privada."""

"""Esta funccion depende de que el usuario 
este autenticado, es decir, depende de que 
el token de acceso sea válido. Si el token 
es válido, se devuelve la información del 
usuario autenticado, de lo contrario, 
se devuelve un error de autenticación."""

@app.get("/users/me")
async def me(user: User = Depends(current_user)):
    return user


"""Form es una clase de FastAPI 
que nos permite capturar los datos 
que se envían a través de un formulario, 
en este caso, el formulario de autenticación 
que se utiliza para enviar el nombre de 
usuario y la contraseña.

Depends es una función de FastAPI que nos 
permite definir dependencias, es decir, 
nos permite definir que una función depende 
de otra función, en este caso, la función 
login depende de la función OAuth2PasswordRequestForm, 
lo que significa que para ejecutar la función login, 
primero se tiene que ejecutar la función 
OAuth2PasswordRequestForm para capturar los datos 
del formulario de autenticación."""

"""access_token es el token de acceso que se devuelve al usuario después de que se ha autenticado correctamente, 
este token se utiliza para acceder a las rutas privadas de la API, es decir, las rutas que requieren autenticación."""

"""La auttenticacion tiene dos formas
la publica y la privada, la publica es 
aquella que no requiere de un token 
para acceder a ella, mientras que la 
privada si requiere de un token para 
acceder a ella. En este caso, las rutas
que hemos definido en este router son públicas, 
ya que no requieren de un token para acceder a ellas. 
Sin embargo, podríamos definir rutas privadas en este 
router si lo deseamos, para ello tendríamos que utilizar 
el parámetro dependencies en el router para definir una 
dependencia que verifique el token antes de permitir el acceso a la ruta.
EJEMPLO: Youtebe: tiene su api pública y su api privada, 
donde puedes ver videos, pero para subir videos necesitas
un token de autenticación, lo que significa que la ruta 
para subir videos es privada, mientras que la ruta para ver videos es pública."""

#QUE ES AUTENTICACION Y QUE ES AUTORIZACION?
"""La autenticación es el proceso de verificar 
la identidad de un usuario, es decir, es el 
proceso de comprobar que el usuario es quien dice ser. 
Esto se hace generalmente a través de un nombre de 
usuario y una contraseña, aunque también se pueden 
utilizar otros métodos como tokens, certificados, etc.

----- AUTORIZACION: es el proceso de verificar si 
un usuario tiene permisos para acceder a un 
recurso o realizar una acción. Esto se hace 
generalmente después de que el usuario ha sido 
autenticado, y se basa en los permisos que se 
le han asignado al usuario. 
Por ejemplo, un usuario puede ser autenticado 
correctamente, pero si no tiene permisos para 
acceder a un recurso, no podrá acceder a él, 
lo que significa que la autorización ha fallado.
"""

"""autenticación basica:
correo y contraseña"""


"""
if not user:	Si no existe usuario
if user is None:	Si usuario es None(nada)
if user.disabled:	Si está deshabilitado
if not user.disabled:	Si está activo
"""