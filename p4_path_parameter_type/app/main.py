from fastapi import FastAPI

app = FastAPI()

@app.get("/product/{product_id}")
async def single_product(product_id:int):
    return {"response":"Single Data Fetched", "product_id":product_id}