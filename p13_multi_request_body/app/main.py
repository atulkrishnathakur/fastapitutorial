from fastapi import FastAPI, Body
from pydantic import BaseModel
from typing import Annotated


app = FastAPI()

# multiple body parameter
class Product(BaseModel):
    name: str
    price: float
    stock: int | None = None

class Seller(BaseModel):
    username: str
    full_name: str | None = None


@app.post("/product")
async def create_product(product:Product, seller: Seller):
    return {"product":product, "seller":seller}


@app.post("/request-optional")
async def request_optional(product:Product, seller: Seller | None = None):
    return {"product":product, "seller":seller}


@app.post("/request-body")
async def request_body(product:Annotated[dict,Body()]):
    return {"product":product}


#Singular value in body
# secret_key is extra value from pydatic model
@app.post("/singular-value-body")
async def singular_value(
    product:Product,
    seller: Seller,
    secret_key: Annotated[str,Body()]
):
    return {
        "product":product,
        "seller":seller,
        "secret_key": secret_key
    }


#with embed
"""
#without embed reqest body like

{
  "name": "string",
  "price": 0,
  "stock": 0
}

# After embed parmeter will be show as key
{
  "product": {
    "name": "string",
    "price": 0,
    "stock": 0
  }
}

"""
@app.post("/with-embed")
async def without_embed(product: Annotated[Product,Body(embed=True)]):
    return product