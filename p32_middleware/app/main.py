from fastapi import FastAPI
from fastapi import Request

app = FastAPI()

#creating middleware
@app.middleware("http")
async def my_first_middleware(request: Request, call_next):
    print("Middleware: Before processing the request")
    print(f"Request: {request.method} {request.url}")
    response = await call_next(request)
    print("Middleware: After processing the request, before returning response")
    print(f"Response status code: {response.status_code}")
    return response


@app.get("/users")
async def get_users():
    print("Endpoint: Inside get_users endpoint")
    return {"data":"All Users Data"}

@app.get("/products")
async def get_products():
    print(f"Endpoint: Inside get_productes endpoint")
    return {"data": "All products data"}