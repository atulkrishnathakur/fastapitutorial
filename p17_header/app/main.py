from fastapi import FastAPI, Header
from typing import Annotated

app = FastAPI()

## Header Parameter
## Header() will read only header it will not set
## run below curl command to set header
'''
atulkrishnathakur@atul-pc:~$ curl -H "User-Agent: Mozila/5.0" http://127.0.0.1:8000/products
'''
@app.get("/products")
async def get_products(user_agent: Annotated[str|None, Header()] = None):
    return user_agent