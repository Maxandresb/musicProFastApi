from datetime import datetime
from pydantic import BaseModel

class Producto(BaseModel):
    id:str
    tipo:str
    categoria:str
    subcategoria:str
    marca:str
    precio:str
    sucursal:str
    fechacreacion:datetime
    fechaactualizacion:datetime