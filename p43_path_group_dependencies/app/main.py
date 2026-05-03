from fastapi import FastAPI, Depends, HTTPException, APIRouter
from typing import Annotated
from routers import router, verify_token

app = FastAPI()

#app.include_router(router) 

app.include_router(router, dependencies=[Depends(verify_token)]) # second way to use dependencies on group of routes

