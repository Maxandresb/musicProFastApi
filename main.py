from datetime import datetime
from conection import db
from fastapi import FastAPI,HTTPException
from models import Producto
import uuid
import json
from types import SimpleNamespace
productos= db.collection(u'productos')


app =FastAPI()

@app.get('/productos')
async def obtenerProductos():
    productosRef=productos.get()
    productosJson={}
    for prod in productosRef:
        productosJson[prod.id]=prod.to_dict()

    return productosJson

@app.get('/productos/{id}')
async def obtenerProducto(id):
    
    productoRef= productos.document(id)
    productJson=productoRef.get()
    return productJson.to_dict()
    

@app.post('/productos')
async def crearProducto(producto: Producto):
    # id= str(uuid.uuid1())
    # print(id)
    # producto.id=id
    now=datetime.now()
    timestampAdd=datetime.timestamp(now)
    productoAdd= productos.document(f'{producto.id}').set(
        {
        'id':producto.id,
        'precio':producto.precio,
        'tipo':producto.tipo,
        'stock':producto.stock
        }
    )
    return {'status':200}


@app.get('/productos/{sucId}/{prodId}')
async def actualizarProducto(sucId,prodId):
    productoRef= productos.document(prodId)
    map(productoRef)
    
       
    
    return {'status':200}
    
    