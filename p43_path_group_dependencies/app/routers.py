from fastapi import APIRouter, Depends, Header, HTTPException
from typing import Annotated

async def verify_token(x_token: Annotated[str, Header()]):
    if x_token != "my-secret-token":
        raise HTTPException(status_code=400, detail="X-Token header invalide")
    

#router = APIRouter(dependencies=[Depends(verify_token)]) # A way to use dependecy on group of routes
router = APIRouter()

@router.get("/items")
async def read_items():
    return {"data":"All items"}

