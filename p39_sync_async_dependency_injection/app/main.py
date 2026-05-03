from fastapi import FastAPI, Depends
from typing import Annotated

app = FastAPI()

# sync dependency
def sync_dep():
    return {"message": "I am sync"}

# async dependency
def async_dep():
    return {"message": "I am async"}


@app.get("/test/")
async def test(
    sync_result: Annotated[dict, Depends(sync_dep)],
    async_result: Annotated[dict, Depends(async_dep)]
):
    return {"sync_data": sync_result, "async_data": async_result}