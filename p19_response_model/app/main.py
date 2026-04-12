from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()

class Product(BaseModel):
    id: int
    name: str
    price: float
    stock: int | None = None

class ProductOut(BaseModel):
    name: str
    price: float


# response_model return data according to defined model like Product 
# response_model priority is high

@app.get("/products",response_model=Product)
async def get_product():
    return {"id":1, "name":"Moto E","price":155.99,  "stock": 12}

@app.get("/products-list",response_model=List[Product])
async def get_product():
    return [
        {"id":1, "name":"Moto E","price":155.99,  "stock": 12},
        {"id":2, "name":"Moto D","price":160.99,  "stock": 25},
        ]


# "response_model_exclude_unset=True" won't be included default values in the response, only the values actually set.
@app.get("/products-exclude",response_model=Product, response_model_exclude_unset=True)
async def get_product():
    return {"id":1, "name":"Moto E","price":155.99}  # stock will not show because stock field not set here




# "response_model_include={"name","price"}" only name and price will go in response from Product model
@app.get("/products-include",response_model=Product, response_model_include={"name","price"})
async def get_product():
    return {"id":1, "name":"Moto E","price":155.99, "stock": 25}  