from fastapi import FastAPI
from fastapi import Depends, Header, HTTPException
from typing import Annotated

async def verify_tokek(x_token: Annotated[str, Header()]):
    if x_token != "my-secret-token":
        raise HTTPException(status_code=400, x_token="X-token Header Invalide")

app = FastAPI(dependencies=[Depends(verify_tokek)])

@app.get("/items")
async def read_items():
    return {"data":"All items"}

@app.get("/products")
async def read_items():
    return {"data":"All products"}