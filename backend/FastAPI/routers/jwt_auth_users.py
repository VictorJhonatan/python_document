from fastapi import Depends, FastAPI, HTTPException, status
from pydantic import BaseModel
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import JWTError, jwt
#from passlib.context import CryptContext
import bcrypt
from datetime import datetime, timedelta

# JWT (JSON Web Token)


#datetime solo para trabajar con fechas y horas (fecha del sistema, fecha de expiración del token, etc)
#timedelta para trabajar con diferentes unidades del tiempo (calculos de fechas, etc)

ALGORITHM = "HS256" 
ACCESS_TOKEN_EXPIRE_MINUTES = 1

#CMD Y PON: openssl rand -hex 32 genera una clave secreta de 32 bytes en formato hexadecimal
SECRET = "be574619c9a15b1e65580155d8a79ec67606d837bd3c77795eb8e8cc122e07ba"
"""SECRET es una clave secreta que se utiliza para firmar y verificar los tokens JWT. Esta clave debe ser mantenida en secreto y no debe ser compartida públicamente, ya que es esencial para la seguridad de los tokens JWT. Al firmar un token JWT, se utiliza esta clave secreta para generar una firma que garantiza la integridad del token y permite verificar su autenticidad. Si un atacante obtiene acceso a esta clave secreta, podría generar tokens JWT falsificados y comprometer la seguridad de la aplicación."""

"""ALGORITHM es el algoritmo de 
cifrado que se utiliza para firmar 
y verificar los tokens JWT, se está
utilizando el algoritmo HS256, que 
es un algoritmo de cifrado simétrico 
basado en HMAC (Hash-based Message 
Authentication Code) con SHA-256 como 
función hash. Este algoritmo es comúnmente 
utilizado para firmar tokens JWT debido a su 
seguridad y eficiencia, se requiere una clave 
secreta compartida entre el emisor del token y 
el receptor para firmar y verificar los tokens 
JWT de manera segura. """

# C:\Users\victo\Documents\python_document\backend\FastAPI\.venv\Scripts\python.exe
""" CTRL + SHIFT + P --> 
Python: Select Interpreter --> seleccionamos 
el intérprete de nuestro entorno virtual (.venv) o---> enter en el path y pones la ruta de arriba
que hemos creado para nuestro proyecto. 
Esto es importante porque nos aseguramos    
de que estamos utilizando las dependencias 
y configuraciones específicas de nuestro proyecto, 
sin interferir con otras instalaciones de Python 
en nuestro sistema. Al seleccionar el intérprete 
del entorno virtual, todas las operaciones relacionadas 
con Python en Visual Studio Code se ejecutarán utilizando 
ese entorno virtual, lo que nos permite mantener un 
entorno de desarrollo limpio y organizado para cada proyecto.

Esto sirve para ejecutar el archivo con el 
intérprete de Python que se encuentra en el e
ntorno virtual (.venv) que hemos creado para nuestro proyecto. 
Al usar este comando, nos aseguramos de que estamos utilizando 
las dependencias y configuraciones específicas de nuestro proyecto, 
sin interferir con otras instalaciones de Python en nuestro sistema."""

app = FastAPI()

oauth2 = OAuth2PasswordBearer(tokenUrl="login")


#contexto de encriptación de contraseñas
"""cryptconext necesita un esquema 
de encriptación para saber cómo 
encriptar las contraseñas, en este 
caso se está utilizando el esquema 
bcrypt, que es un algoritmo de hashing 
de contraseñas recomendado por la comunidad 
de seguridad. bcrypt es resistente a ataques 
de fuerza bruta y es ampliamente utilizado 
para proteger contraseñas en aplicaciones web. 
Al configurar el contexto de encriptación con bcrypt, 
se asegura que las contraseñas se encripten de manera 
segura antes de almacenarlas en la base de datos, y 
luego se puedan verificar correctamente durante el 
proceso de autenticación."""
#crypt = CryptContext(schemes=["bcrypt"], deprecated="auto")
#crypt = bcrypt

class User(BaseModel):
    username: str
    full_name : str
    email: str
    disabled: bool

class UserInDB(User):
    password: str

user_db = {

    "victor": {
        "username": "victor",
        "full_name": "Victor Robles",
        "email": "victor@victor.com",
        "disabled": False,
        "password": "$2a$12$l53NFtRjBd.ULDwhszL5Pe47BEtnluKagdDUG8F4zGY8e78Cr9sDK"
    },

    "analu": {
        "username": "ana",
        "full_name": "Ana García",
        "email": "ana@ana.com",
        "disabled": True,
        "password": "$2a$12$lxxRoVDJl4d0.fzT8hJwwuMVUDpIUv3QuWoJ66itpqbUwbR9bg2Fa"
    },

    "luis": {
        "username": "luis",
        "full_name": "Luis Martínez",
        "email": "luis@luis.com",
        "disabled": False,
        "password": "$2a$12$i/0sURl7bvxnKJliK82gxekBT7We91hiaUIWWlxlz17P8Bpofn/gS"
    }
}

def search_user(username: str):
    if username in user_db:
        return UserInDB(**user_db[username]) # **user_db[username] es una forma de desempaquetar el diccionario que se encuentra en user_db[username], lo que significa que se están pasando los valores del diccionario como argumentos a la clase UserInDB para crear una instancia de esa clase con esos valores. Por ejemplo, si username es "victor", entonces user_db[username] es el diccionario {"username": "victor", "full_name": "Victor Robles", "email": "

#fun sin la contraseña, entrega todos los datos del usurio pero sin su contraseña
def search_users(username: str):
    if username in user_db:
        return User(**user_db[username])
    

# esta funtion sirve para verificar si el token JWT es válido y para obtener la información del usuario autenticado a partir del token. La función auth_user es una función de dependencia que se utiliza en otras funciones para proteger rutas y asegurarse de que solo los usuarios autenticados puedan acceder a ellas. Si el token JWT es válido, la función devuelve la información del usuario autenticado, de lo contrario, lanza una excepción de autenticación.
#seunda dependencia(obtenemos el token y lo verificamos) de get al buscar el token
async def auth_user(token: str = Depends(oauth2)):

    exception = HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, 
            detail="credenciales  de autenticación inválidas", 
            headers={"WWW-Authenticate": "Bearer"})
    
    try:
        #desemcriptamos el token para obtener el nombre de usuario, jwt.decode decodifica el token JWT utilizando la clave secreta y el algoritmo especificados. Si el token es válido y la firma es correcta, devuelve el contenido del token como un diccionario. En este caso, se espera que el token contenga información sobre el usuario autenticado, como su nombre de usuario (sub) y la fecha de expiración (exp). Si el token no es válido o ha expirado, se lanzará una excepción que se puede manejar para devolver un error de autenticación.
        username = jwt.decode(token, SECRET, algorithms=[ALGORITHM]).get("sub") # jwt.decode decodifica el token JWT utilizando la clave secreta y el algoritmo especificados. Si el token es válido y la firma es correcta, devuelve el contenido del token como un diccionario. En este caso, se espera que el token contenga información sobre el usuario autenticado, como su nombre de usuario (sub) y la fecha de expiración (exp). Si el token no es válido o ha expirado, se lanzará una excepción que se puede manejar para devolver un error de autenticación.
        if username is None:
            raise exception
    
    except JWTError:
        raise exception
    
    return search_users(username)

# sirve para verificar si el usuario autenticado está activo o no. Si el usuario está deshabilitado, se lanza una excepción de error con un mensaje indicando que el usuario está inactivo. Si el usuario está activo, se devuelve la información del usuario autenticado. Esta función se utiliza como una dependencia en las rutas protegidas para asegurarse de que solo los usuarios activos puedan acceder a ellas.
#1ra dependencia de get al buscar el token
async def current_user(user: User = Depends(auth_user)): 
    if user.disabled:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Usuario inactivo")
    return user


@app.post("/login")
async def login(form: OAuth2PasswordRequestForm = Depends()):
    users_db = user_db.get(form.username)
    if not users_db:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="El usuario no es correcto")
    
    user = search_user(form.username)

    #METODO ANTIGUO DE VERIFICAR CONTRASEÑA
    #if not (form.password, user.password): # verifica si la contraseña es correcta
        #raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Contraseña incorrecta")
    
    #METODO NUEVO DE VERIFICAR CONTRASEÑA CON BCRYPT
    if not bcrypt.checkpw(form.password.encode("utf-8"), user.password.encode("utf-8")): #.checkpw verifica si la contraseña es correcta, form.password.encode("utf-8") convierte la contraseña ingresada por el usuario a bytes, user.password.encode("utf-8") convierte la contraseña almacenada en la base de datos a bytes, y bcrypt.checkpw compara ambas contraseñas encriptadas para verificar si coinciden.
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Contraseña incorrecta")
    

    #sumar hora actual + el tiempo de expiración del token ---> datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    #datetime.utcnow() devuelve fecha y hora actual en formato UTC (Coordinated Universal Time), que es un estándar de tiempo utilizado en todo el mundo. Al usar datetime.utcnow(), se obtiene la fecha y hora actual en UTC, lo que es útil para evitar problemas de zona horaria al trabajar con fechas y horas en aplicaciones web.
    
    acces_token = {"sub": user.username, 
                   "exp": datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)} 
    # sub es el sujeto del token, en este caso el nombre de usuario, exp es la fecha de expiración del token

    return {"access_token": jwt.encode(acces_token, SECRET, algorithm=ALGORITHM), "token_type": "bearer"}



@app.get("/users/me")
async def me(user: User = Depends(current_user)):
    return user





# pip install pyjwt
"""Sirve para crear y verificar 
tokens JWT (JSON Web Tokens), 
que son una forma de representar 
información de forma segura y compacta. 
En este caso, lo utilizamos para crear 
tokens de acceso para los usuarios que 
se autentican en la aplicación, y 
luego verificar esos tokens para 
permitir el acceso a rutas protegidas."""

# pip install "pwdlib[argon2]"
"""Sirve para encriptar contraseñas 
de forma segura utilizando el algoritmo Argon2, 
que es un algoritmo de hashing de contraseñas 
recomendado por la comunidad de seguridad. 
En este caso, lo utilizamos para encriptar 
las contraseñas de los usuarios antes de 
almacenarlas en la base de datos, y 
luego verificar esas contraseñas en el 
proceso de autenticación."""

""" pip install "passlib[bcrypt]
Sirve para encriptar contraseñas de forma segura utilizando el algoritmo bcrypt, que es otro algoritmo de hashing de contraseñas recomendado por la comunidad de seguridad. En este caso, lo utilizamos para encriptar las contraseñas de los usuarios antes de almacenarlas en la base de datos, y luego verificar esas contraseñas en el proceso de autenticación. bcrypt es conocido por ser resistente a ataques de fuerza bruta y es ampliamente utilizado para proteger contraseñas en aplicaciones web."""

# # Instala los paquetes
# pip install fastapi uvicorn pydantic python-jose[cryptography] passlib[bcrypt]