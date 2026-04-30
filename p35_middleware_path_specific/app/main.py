from fastapi import FastAPI
from middleware import users_only_middleware, product_only_middleware

app = FastAPI()

# ****** this is a way to add function middleware ***********
app.middleware("http")(users_only_middleware)
app.middleware("http")(product_only_middleware)

@app.get("/users")
async def get_users():
    print("Endpoint: Inside get_users endpoint")
    return {"data":"All Users Data"}

@app.get("/products")
async def get_products():
    print(f"Endpoint: Inside get_productes endpoint")
    return {"data": "All products data"}