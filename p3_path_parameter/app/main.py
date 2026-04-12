from fastapi import FastAPI

app = FastAPI()

@app.get("/product")
async def all_products():
    return {"response":"All products"}

@app.get("/product/{product_id}")
async def single_product(product_id:int):
    return {"response":"Single Product Data","product_id":product_id}


@app.post("/product")
async def create_product(new_product: dict):
    return {"response":"Product Created","new_product":new_product}


@app.put("/product/{product_id}")
async def update_product(new_updated_product: dict, product_id:int):
    return {
            "response":"Product Updated",
            "new updated product":new_updated_product,
            "product_id":product_id
        }

@app.patch("/product/{product_id}")
async def partial_update_product(new_updated_product: dict, product_id:int):
    return {
            "response":"Product updated",
            "new updated product":new_updated_product,
            "product_id":product_id
        }


@app.delete("/product/{product_id}")
async def delete_product(product_id:int):
    return {
            "response":"Product deleted",
            "product_id":product_id
        }