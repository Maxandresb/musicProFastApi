from datetime import datetime
from pydantic import BaseModel

class Producto(BaseModel):
    id:int
    precio:int
    tipo:str
    stock:dict

