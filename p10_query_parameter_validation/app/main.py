from fastapi import FastAPI, Query
from typing import Annotated
from pydantic import AfterValidator

app = FastAPI()

PRODUCTS = [
        {
            "id": 1,
            "title": "Fjallraven - Foldsack No. 1 Backpack, Fits 15 Laptops",
            "price": 109.95,
            "description": "Your perfect pack for everyday use and walks in the forest. Stash your laptop (up to 15 inches) in the padded sleeve, your everyday"
        },
        {
            "id": 2,
            "title": "Mens Casual Premium Slim Fit T-Shirts",
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


@app.get("/products")
async def get_products(search:str | None = None):
    if search:
        search_lower = search.lower()
        filtered_products = []
        for product in PRODUCTS:
            if search_lower in product["title"].lower():
                filtered_products.append(product)
        return filtered_products
    return PRODUCTS


@app.get("/products_query")
async def get_products_q(search:str | None = Query(default=None,max_length=5)):
    """
    This is the old way to use Query
    """
    if search:
        search_lower = search.lower()
        filtered_products = []
        for product in PRODUCTS:
            if search_lower in product["title"].lower():
                filtered_products.append(product)
        return filtered_products
    return PRODUCTS


@app.get("/products_query_annotated")
async def get_products_anno(search:Annotated[str | None, Query(max_length=15, min_length=5,  pattern="^[a-z]+$")]=None):
    """
    Annotated is the good way to use Query
    """
    if search:
        search_lower = search.lower()
        filtered_products = []
        for product in PRODUCTS:
            if search_lower in product["title"].lower():
                filtered_products.append(product)
        return filtered_products
    return PRODUCTS


@app.get("/products_query_annotated_alias")
async def get_products_anno_alias(search: Annotated[str|None,Query(alias='q')] = None):
    if search:
        filtered_products = []
        for product in PRODUCTS:
            for s in search:
                if s.lower() in product['title'].lower():
                    filtered_products.append(product)
        return filtered_products
    return PRODUCTS


#custom validation

def check_valid_id(id: str):
    if not id.startswith("prod-"):
        raise ValueError("ID must start with 'prod-'")
    return id


@app.get("/products_custom_validation")
async def get_products_custom_validation(id: Annotated[str|None,AfterValidator(check_valid_id)] = None):
    if id:
        return {"id":id, "message":"Valid product ID"}
    return {"message":"No ID Provided"}