from fastapi import FastAPI, Header, Depends
from typing import Annotated
from fastapi import HTTPException

app = FastAPI()

# Dependencies is path operation decorators
async def verify_token(x_token: Annotated[str,Header()]):
    if x_token != "my-secret-token":
        raise HTTPException(status_code=400, detail="X-Token header invalid")


@app.get("/items", dependencies=[Depends(verify_token)])
async def read_items():
    return {"data": "All Items"}