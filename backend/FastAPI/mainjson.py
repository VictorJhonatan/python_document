from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import json

app = FastAPI()

# Modelo del usuario (estructura del body)
class User(BaseModel):
    id: int
    name: str
    surname: str
    age: int
    url: str

with open("mi_json.json", "r", encoding="utf-8") as mi_other_file:
    datos = json.load(mi_other_file)

#metodo GET
@app.get("/userjson/{id}")
async def users(id: int):
    return search_user(id)

#METHOD POST
@app.post("/userjson/",response_model=User, status_code=201) 
async def users(user: User):
    
    #Buscar si el ID ya existe
    for u in datos["users"]:
        if u["id"] == user.id:
            raise HTTPException(status_code=404, detail="El usuario ya existe") 
    
    datos["users"].append(user.dict()) # .dict() convierte el objeto user en un diccionario para poder guardarlo en el JSON
    with open("mi_json.json", "w", encoding="utf-8") as mi_other_file:
        json.dump(datos, mi_other_file, indent=4) #dump() convierte el diccionario en un JSON y lo guarda en el archivo, indent=4 es para que el JSON se vea más bonito
    return user

"""HTTPException es una clase que se 
utiliza para manejar las excepciones 
en FastAPI. En este caso, estamos 
utilizando HTTPException para devolver 
un error 404 cuando el usuario ya existe. 
El parámetro status_code es el código de 
estado HTTP que se devolverá, y el
 parámetro detail es el mensaje de error 
 que se devolverá en el cuerpo de la respuesta."""

"""El raison por la que utilizamos 
HTTPException en lugar de 
return {"error": "El usuario ya existe"} 
es porque HTTPException nos permite 
devolver un código de estado HTTP específico, 
lo que es más adecuado para manejar errores en una API.
"""

#METHOD PUT
@app.put("/userjson/")
async def user(user: User):
    found = False

    for index, save_user in enumerate(datos["users"]):
        if save_user["id"] == user.id:
            datos["users"][index] = user.dict() # .dict() convierte el objeto user en un diccionario para poder guardarlo en el JSON
            found = True
            with open("mi_json.json", "w", encoding="utf-8") as mi_other_file:
                json.dump(datos, mi_other_file, indent=4) #dump() convierte el diccionario en un JSON y lo guarda en el archivo, indent=4 es para que el JSON se vea más bonito
            return user
    if found == False: # if not found: es lo mismo que if found == False:
        return {"error": "Usuario no Actualizado"}

#METHOD DELETE
@app.delete("/userjson/{id}")
async def user(id: int):
    found = False
    for index, save_user in enumerate(datos["users"]):
        if save_user["id"] == id:
            del datos["users"][index]
            found = True
            with open("mi_json.json", "w", encoding="utf-8") as mi_other_file:
                json.dump(datos, mi_other_file, indent=4) #dump() convierte el diccionario en un JSON y lo guarda en el archivo, indent=4 es para que el JSON se vea más bonito
            return {"message": "Usuario Eliminado"}
    if not found:
            return {"error": "Usuario no Eliminado"}

#función para buscar un usuario por su ID
def search_user(id: int):
    users = filter(lambda user: user["id"] == id, datos["users"])
    try:
        return list(users)[0]
    except IndexError:
        return {"error": "Usuario no encontrado"}
    

