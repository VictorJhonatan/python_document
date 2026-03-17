from fastapi import APIRouter
from pydantic import BaseModel #importante para definir modelos de datos


class user(BaseModel): # este argumento me da la capacidad de crear una entidad(entidad es un objeto con propiedades)
    id: int
    name: str
    surname: str
    age: int
    url: str

users_list = [
    user(id=1, name="Victor", surname="Robles", age=35, url="http://arknodev.com"),
    user(id=2, name="Ana", surname="Gonzalez", age=28, url="http://anagonzalez.com"),
    user(id=3, name="Luis", surname="Martinez", age=42, url="http://luismartinez.com")
    ]

app = APIRouter()


@app.get("/userjson")
async def users():
    return users_list

"""path operation es una función que se 
ejecuta cuando se accede a una ruta 
específica en la aplicación web.
En FastAPI, se define una path 
operation utilizando decoradores 
como @app.get(), @app"""
#path operation - endpoint - ruta de acceso

@app.get("/user/{id}")
async def userss(id: int):
    return search_user(id)

#path operation con path parameter - parametro de ruta
@app.get("/userss/{name}")
async def usuario(name: str):
    users = filter(lambda user: user.name == name, users_list) #user.name es el nombre del atributo de la clase user, name es el argumento de la funcion usuario, users_list es la lista de usuarios que tenemos definida al principio del codigo
    try:
        return list(users)[0]
    except IndexError:
        return {"error": "Usuario no encontrado"}
    
# query parameter - parametro de consulta
""" Un query parameter es un valor que se 
pasa a través de la URL después del signo 
de interrogación (?). 
Se utiliza para enviar información adicional 
al servidor cuando se realiza una solicitud HTTP.
En FastAPI, puedes definir query parameters 
en tus path operations utilizando argumentos de función."""
# query parameter - parametro de consulta

@app.get("/userquery/") # http://127.0.0.1:8000/userquery?id=1
async def usuario(id: int):
    return search_user(id)
    
def search_user(id: int):
    users = filter(lambda user: user.id == id, users_list)
    try:
        return list(users)[0]
    except IndexError:
        return {"error": "Usuario no encontrado"}


"""Las urls son dinaminas, es decir, 
pueden tener parametros que se pueden 
usar para buscar o filtrar informacion,"""

"""OJO: Usamos el path cuando las urls 
son fijas como /user/{id}, 
y las query que pueden no ser 
necesarios para una peticion como /userquery?id=1, 
el query es opcional, el path no es opcional, 
el path es obligatorio, el query es opcional, 
el path es para identificar un recurso especifico"""

