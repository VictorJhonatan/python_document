from fastapi import APIRouter #APIRouter es una clase de FastAPI que nos permite crear rutas de forma modular, es decir, podemos crear diferentes routers para diferentes partes de nuestra aplicación y luego incluirlos en el main.py para que estén disponibles en toda la aplicación.

""" QUE ES UN ROUTER EN FASTAPI?
los routers son una forma de 
organizar el código en FastAPI, 
es decir, son una forma de 
dividir el código en diferentes 
archivos para que sea más fácil 
de mantener y entender. En este 
caso, hemos creado un router 
para los productos, pero podríamos 
crear otros routers para los usuarios, las órdenes, etc.
"""

router = APIRouter(prefix="/products", tags=["products"], responses={404: {"message": "No encontrado"}}) 
""" QUE ES EL PREFIX EN UN ROUTER DE FASTAPI?
prefix es un parámetro que se 
utiliza para definir un prefijo 
común para todas las rutas que se 
definan en este router. En este caso, 
todas las rutas que se definan en este 
router tendrán el prefijo "/products", 
lo que significa que para acceder a 
estas rutas, tendremos que escribir 
"/products" seguido de la ruta específica.
Por ejemplo, si definimos una ruta "/list" 
en este router, para acceder a esa ruta, 
tendremos que escribir "/products/list".
"""

""" QUE ES EL TAGS EN UN ROUTER DE FASTAPI?
tags es un parámetro que se utiliza 
para definir una etiqueta para las 
rutas que se definan en este router. 
Esta etiqueta se utiliza para organizar 
las rutas en la documentación automática 
de FastAPI, lo que facilita la navegación 
y comprensión de la API. En este caso, 
hemos definido el tag "products" para 
todas las rutas de este router, lo que 
significa que en la documentación automática 
de FastAPI, todas las rutas de este router 
estarán agrupadas bajo la etiqueta "products". 
"""

""" QUE ES EL RESPONSES EN UN ROUTER DE FASTAPI?
responses es un parámetro que 
se utiliza para definir las 
respuestas que se pueden devolver 
en caso de que ocurra un error. En 
este caso, hemos definido una 
respuesta para el código de estado 404, 
que indica que el recurso no fue encontrado."""

products_list = ["Producto 1", "Producto 2", "Producto 3", "Producto 4", "Producto 5"]

@router.get("/")
async def products():
    return products_list

@router.get("/{id}")
async def products(id: int):
    return products_list[id]



