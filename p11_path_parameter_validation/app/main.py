from fastapi import FastAPI, Path, Query
from typing import Annotated
from pydantic import AfterValidator

app = FastAPI()

PRODUCTS = [
        {
            "id": 1,
            "title": "books",
            "price": 109.95,
            "description": "Your perfect pack for everyday use and walks in the forest. Stash your laptop (up to 15 inches) in the padded sleeve, your everyday"
        },
        {
            "id": 2,
            "title": "foods",
            "price": 22.3,
            "description": "Slim-fitting style, contrast raglan long sleeve, three-button henley placket, light weight & soft fabric for breathable and comfortable wearing. And Solid stitched shirts with round neck made for durability and a great fit for casual fashion wear and diehard baseball fans. The Henley style round neckline includes a three-button placket."
        },
        {
            "id": 3,
            "title": "Mens Cotton Jacket",
            "price": 55.99,
            "description": "great outerwear jackets for Spring/Autumn/Winter, suitable for many occasions, such as working, hiking, camping, mountain/rock climbing, cycling, traveling or other outdoors. Good gift choice for you or your family member. A warm hearted love to Father, husband or son in this thanksgiving or Christmas Day."
        },
    ]


# basic path parameter validation
@app.get('/products/{product_id}')
async def get_product(product_id:int):
    for product in PRODUCTS:
        if product['id'] == product_id:
            return product
        return {"error":"Product not found"}
    

# Numeric validation
@app.get('/products-validation/{product_id}')
async def get_product_num_validation(product_id: Annotated[int, Path(ge=1,le=10)]):
    for product in PRODUCTS:
        if product['id'] == product_id:
            return product
    return {"error":"Product not found"}


# meta data
@app.get('/products-metadata/{product_id}')
async def get_product_metadata(product_id: Annotated[int, Path(title="The ID of the product",description="This is product id")]):
    for product in PRODUCTS:
        if product['id'] == product_id:
            return product
    return {"error":"Product not found"}



# combining path and query parameter
@app.get('/products-path-query/{product_id}')
async def get_product_metadata(
    product_id: Annotated[int, Path(gt=0,le=100,)],
    search: Annotated[str|None, Query(max_length=200)] = None
):
    for product in PRODUCTS:
        if search and search.lower() not in product['title'].lower():
            return {"error":"Product does not match search term"}
        return product
    
    return {"error":"Product not found"}