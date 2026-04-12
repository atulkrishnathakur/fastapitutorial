from fastapi import FastAPI, Cookie
from typing import Annotated

app = FastAPI()


# by swagger we can not set cookie
# Cookie() only use to read Cookie not set
# set command by using curl command see below command
# curl -H "Cookie: session_id=abc123" http://127.0.0.1:8000/products/recommendation
@app.get("/products/recommendation")
async def get_recommendations(session_id:Annotated[str | None,Cookie()] = None):
    if session_id:
        return {"message":f"Recommendations for session {session_id}","session_id":session_id}
    
    return {"message": "No, Session ID provided, Showing default recomendations"}