from fastapi import FastAPI, Body
from pydantic import BaseModel, Field
from typing import Annotated

app = FastAPI()

## pydantic field
class Product(BaseModel):
    name: str = Field(
        title="Product name",
        description="The name of the product",
        max_length=100,
        min_length=5, 
        pattern="^[A-Za-z0-9]+$"
    )
    price: float = Field(
        gt=0,
        title="Product Price",
        description="Value will be greater than zero"
    )
    stock: int | None = Field(
        default=None,
        title="Stock Quantity",
        description="The number of item in stock, must be none negative"
    )


@app.post("/product")
async def create_product(product:Product):
    return product