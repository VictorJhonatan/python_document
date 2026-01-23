from fastapi import FastAPI



app = FastAPI() 
#get se usa para obtener algo traer algo en este caso a HTTP
@app.get("/") #IP de la web o del servidor es el localhost 

async def root():
    return "Hola desde main:---> FastAPI--ARKANO1q"

@app.get("/url") 
async def root():
    return {"url_curso": "http://arknodev.com/python"}

# {"dateils": "Not Found"} - cuando no encuentra la ruta
# 404 - cuando no encuentra la ruta
"""seguir los protocolos de internet ( http ) 
saber manejar los codigos como 200, 404, 500 etc
ejemplo: hey dame este usuario con id 1, pero si 
no encuentra el id 1 del usuario nos da un JSON
con el mensaje de que no lo ha encontrado y 
ese es el codigo 404

el codigo 500 es error no sabe manejar la 
peticion, el servidor tiene un error interno, 
ejemplo
el servidor se ha caido, el servidor no responde, 
el servidor no sabe que hacer con la peticion, 
eso pasa cuando el servidor tiene un error interno"""

"""Ahora nos devuelve return 
pero a donde va estar escuchando 
esta llamada del servidor, cual es 
la url que tenemos que llamar y de 
que forma llamarlo, accedemos con @ 
este @ entra al contexto de fastAPI y llama a get 
Ahora tener claro 
--------esta funcion no debe ser sincrona, 
debe ser asincrona, cada ves que llames al servidor 
la operacion debe ser asincrona, que es sincrono.
si tienes una peticion sincrona osea desde la web 
o el movil llamas al servidor y la app no hace nada 
hasta que retorne algo el servidor, entonces no debe 
ser sincrono debe ser asincrona porque llamas al 
servidor pero no sabes si el servidor cuanto va tardar, 
sabes de algo que no tienes control, 

si estas navegando en la web y te llega una notificacion, 
no ha estado bloqueada, ha llegado al backend y le ha 
dicho que lo muestre en la web

ENTONCES: FUNTION root de ser asincrono, 
para que funcione y haga lo que quiera 
y lo que tenga que hacer cuando pueda, 
muchas personas se pueden conectar y 
hacer muchas cosas o tu mismo haces 
muchas cosas pero en segundo plano, va
devolver datos(cosas) en segundo plano, por eso hace lo que quiere
OJO: DESPUES DE USAR EL PROTOCOLO 
PARA CONECTARTE A INTERNET o la RED 
|--------------QUE ES EL ESTANDAR HTTP para llamar a la web
# uvicorn main:app este main nombre del fichero, 
# y app es la instancia que tiene la variable que tiene fastAPI. 
# -- reload recargar el contexto del servidor cada ves que 
# cambie algo en el fichero,osea como si uvicron actuliza en 
# tiempo real, y ya no recargar"""

"""dos formas: de cargar la web con uvicorn
python -m uvicorn main:app --reload 
uvicorn main:app --reload"""


"""OJO: swagger es una interfaz grafica
que nos permite interactuar con nuestra API de
manera visual, es decir, podemos ver los endpoints( endpoints son las rutas )
disponibles, probar las peticiones HTTP
(GET, POST, PUT, DELETE, etc.), ver la documentación
get: es para obtener datos
post: es para enviar datos
put: es para actualizar datos
delete: es para eliminar datos
y ver las respuestas de la API directamente desde el navegador.
Esto facilita mucho el desarrollo y la prueba de APIs,"""


