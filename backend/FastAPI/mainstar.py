from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from routers import products
from routers import users
from fastapi.staticfiles import StaticFiles 
"""fastapi.staticfiles es un módulo de FastAPI 
que nos permite servir archivos estáticos, 
como imágenes, CSS, JavaScript, etc. 
En este caso, lo utilizamos para servir los 
archivos de la carpeta "static" que se 
encuentra en el mismo nivel que el archivo 
"""
app = FastAPI()

#routers
app.include_router(products.router) # .router porque es el nombre del router que hemos creado en products.py
app.include_router(users.app) # .app porque es el nombre del router que hemos creado en users.py
app.mount("/static", StaticFiles(directory="static"), name="static") 

""" QUE ES EL MOUNT EN FASTAPI?
es un método de FastAPI que nos permite 
montar una ruta para servir archivos 
estáticos. En este caso, hemos montado 
la ruta "/static" para servir los 
archivos de la carpeta "static". 
Esto significa que si queremos 
acceder a un archivo que se encuentra 
en la carpeta "static", tendremos que 
escribir "/static/nombre_del_archivo". 
Por ejemplo, si tenemos un archivo llamado 
"imagen.jpg" en la carpeta "static", para 
acceder a ese archivo, tendremos que escribir "/static/imagen.jpg".
"""

"""que es staticfiles(directory="static")?
staticfiles es una clase de FastAPI 
que nos permite servir archivos estáticos.
El parámetro directory se utiliza para 
especificar la carpeta donde se encuentran 
los archivos estáticos que queremos,
en este caso, la carpeta "static", 
name es un parámetro que se utiliza 
para darle un nombre a la ruta que
estamos montando, en este caso, "static".
"""

class User(BaseModel):
    id: int
    name: str
    surname: str
    age: int
    url: str
    
users_list = [
    User(id=1, name="Victor", surname="Robles", age=35, url="http://arknodev.com"),
    User(id=2, name="Ana", surname="Gonzalez", age=28, url="http://anagonzalez.com"),
    User(id=3, name="Luis", surname="Martinez", age=42, url="http://luismartinez.com")
    ]


#QUERY
@app.get("/user/")
async def userss(id: int): 
    return search_user(id)  

#METHOD POST
@app.post("/userjson/", status_code=201)
async def users(user: User):
    if type(search_user(user.id)) == User:
        return {"error": "El usuario ya existe"}
    users_list.append(user)
    return user


#METHOD PUT
@app.put("/userjson/")
async def user(user: User):
    found = False

    for index, save_user in enumerate(users_list):
        if save_user.id == user.id:
            users_list[index] = user
            found = True
    if not found:
        return {"error": "Usuario no Actualizado"}
    return user

@app.delete("/userjson/{id}")
async def user(id: int):
    found = False
    for index, save_user in enumerate(users_list):
        if save_user.id == id:
            del users_list[index]
            found = True
            return {"message": "Usuario Eliminado"}
    if not found:
            return {"error": "Usuario no Eliminado"}
    
            
def search_user(id: int):
    users = filter(lambda user: user.id == id, users_list)
    try:
        return list(users)[0]
    except IndexError:
        return {"error": "Usuario no encontrado"}
    
