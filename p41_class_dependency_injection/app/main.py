from fastapi import FastAPI, Depends
from typing import Annotated

app = FastAPI()

# Creatign Dependancy Class

class CommonQueryParam:
    def __init__(self, q: str | None = None, skip: int=0, limit: int = 100):
        self.q = q
        self.skip = skip
        self.limit = limit


# Using dependency in endpoints
@app.get("/items")
async def read_item(commons: Annotated[CommonQueryParam, Depends(CommonQueryParam)]):
    return commons


@app.get("/items")
async def read_users(commons: Annotated[CommonQueryParam, Depends(CommonQueryParam)]):
    return commons


# create type alias 
CommonsDep = Annotated[CommonQueryParam, Depends(CommonQueryParam)]

@app.get("/products")
async def read_product(commons: CommonsDep):
    return commons

@app.get("/carts")
async def read_carts(commons: CommonsDep):
    return commons