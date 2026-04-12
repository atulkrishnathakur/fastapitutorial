from fastapi import FastAPI, Cookie
from pydantic import BaseModel, Field
from typing import Annotated

app = FastAPI()

class ProductCookie(BaseModel):
    session_id: str 
    preferred_category: str | None = None
    tracking_id: str | None = None


# Cookie() not use to set. It read Cookie() only
# By swagger we can not read cookie by Cookie()
# set cookie by curl check below command
# curl -H "Cookie: session_id=abc123; preferred_category=Electronics; tracking_id=xyz789" http://127.0.0.1:8000/products/recommendations


"""
if you run: 
atulkrishnathakur@atul-pc:~$ curl -H "Cookie: preferred_category=Electronics; tracking_id=xyz789" http://127.0.0.1:8000/products/recommendations

Then it give required error becouse session_id field is not set
"""



## forbidding extra cookie
class ProductCookieForbid(BaseModel):
    model_config = {"extra": "forbid"}
    session_id: str 
    preferred_category: str | None = None
    tracking_id: str | None = None


"""
If you set:
model_config = {"extra": "forbid"}

you can not set extra field
"""


@app.get("/products/recommendations")
async def get_recommendations(cookies: Annotated[ProductCookie,Cookie()]=None):
    response = {"session_id": cookies.session_id}
    if cookies.preferred_category:
        response["message"] = f"Recommendations for {cookies.preferred_category} products"
    else:
        response["message"] = f"Default recommendations for {cookies.session_id}"
    return response