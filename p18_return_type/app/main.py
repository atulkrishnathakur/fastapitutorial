from fastapi import FastAPI
from pydantic import BaseModel
from typing import Annotated, List

app = FastAPI()

class Product(BaseModel):
    id: int
    name: str
    price: float
    stock: int | None = None


# return type
@app.get("/products")
async def get_products() -> Product:
    return {"id":1, "name":"Mote E", "price": 33.34, "stock": 5}



# return type
@app.get("/products-list")
async def get_products_list() -> List[Product]:
    return [
        {"id":1, "name":"Mote E", "price": 33.34, "stock": 5},
        {"id":2, "name":"Mote D", "price": 55.34, "stock": 10},
    ]