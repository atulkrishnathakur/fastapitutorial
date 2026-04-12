from fastapi import FastAPI
from typing import List, Tuple
from pydantic import BaseModel

app = FastAPI()

#create or insert data
@app.post("/product")
async def create_product(new_product:dict):
    return new_product


#create or insert data
@app.post("/product2")
async def create_product2(new_product:list[str]):
    return new_product


#create or insert data
@app.post("/product3")
async def create_product3(new_product:Tuple[str,int]):
    return new_product


# define a base model

class Product(BaseModel):
    id: int
    name: str
    price: float
    stock: int | None = None #optional

#create or insert with pydantic
@app.post("/product4")
async def create_product4(new_product:Product):
    return new_product


#create or insert with pydantic
@app.post("/product5")
async def create_product5(new_product:Product):
    return new_product.name


# add new field in dictionary
@app.post("/update_new_field_in_dict")
async def update_new_field_in_dict(new_product:Product):
    product_dict = new_product.model_dump()
    price_with_tax = new_product.price + (new_product.price * 18 / 100)
    product_dict.update({"price_with_tax":price_with_tax})
    return product_dict


# combining request body with path parameter
@app.put("/body_and_path/{product_id}")
async def update_product(product_id:int, new_updated_product: Product):
    return {
        "product_id":product_id,
        "new_updated_product":new_updated_product
    }


# combining request body with path parameter
@app.put("/body_path_query/{product_id}")
async def update_product(product_id:int, new_updated_product: Product, discount: float | None = None):
    return {
        "product_id":product_id,
        "new_updated_product":new_updated_product,
        "discount": discount
    }