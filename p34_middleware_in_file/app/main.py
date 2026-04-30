from fastapi import FastAPI
from middleware import my_first_middleware, my_second_middleware

app = FastAPI()

# ****** this is a way to add function middleware ***********
app.middleware("http")(my_first_middleware)
app.middleware("http")(my_second_middleware)

@app.get("/users")
async def get_users():
    print("Endpoint: Inside get_users endpoint")
    return {"data":"All Users Data"}

@app.get("/products")
async def get_products():
    print(f"Endpoint: Inside get_productes endpoint")
    return {"data": "All products data"}