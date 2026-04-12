from fastapi import FastAPI

app = FastAPI()



@app.get("/product/hard_coded_titile")
async def single_product_hardcoded():
    return {"response":"Hard coded path"}

@app.get("/product/{product_title}")
async def single_product_hardcoded(product_title):
    return {"response":"Dynamic data fetch","title":product_title}

# If path is same and some time you use dynaic and some time use hard coded then hard coded route write first dynamic route.


