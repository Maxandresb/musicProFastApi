from datetime import datetime
from conection import db
from fastapi import FastAPI,HTTPException
from models import Producto
import uuid

productos= db.collection(u'productos')


app =FastAPI()

@app.get('/productos')
async def root():
    productosRef=productos.get()
    productosJson={}
    for prod in productosRef:
        productosJson[prod.id]=prod.to_dict()

    return productosJson

@app.post('/productos')
async def crearProducto(producto: Producto):
    id= str(uuid.uuid1())
    print(id)
    producto.id=id
    now=datetime.now()
    timestampAdd=datetime.timestamp(now)
    productoAdd= productos.document(f'{producto.id}').set(
        {
        'id':producto.id,
        'tipo':producto.tipo,
        'categoria':producto.categoria,
        'subcategoria':producto.subcategoria,
        'marca':producto.marca,
        'precio':producto.precio,
        'sucursal':producto.sucursal,
        'fechacreacion':timestampAdd,
        'fechaactualizacion':timestampAdd,
        }
    )
