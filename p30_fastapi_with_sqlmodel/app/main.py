from fastapi import FastAPI
from app.user.models import User
from app.product.models import Product
from app.db.config import create_table
from contextlib import asynccontextmanager

@asynccontextmanager
async def lifespan(app: FastAPI):
    create_table()
    yield

app = FastAPI(lifespan=lifespan)