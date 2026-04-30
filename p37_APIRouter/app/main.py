from fastapi import FastAPI
from user.routers import router as user_routers
from product.routers import router as product_router


app = FastAPI()

app.include_router(user_routers, tags=['users'], prefix='/users')
app.include_router(product_router, tags=["products"])