from fastapi import FastAPI
from enum import Enum

app = FastAPI()

class ProductCategory(str, Enum):
    books = "Books"
    clothing="clothing"
    electronics="electronics"

@app.get("/product/{category}")
async def get_product(category: ProductCategory):
    return {"response":"Product Fetched", "category":category}