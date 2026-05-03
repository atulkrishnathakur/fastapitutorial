from fastapi import FastAPI, Depends, HTTPException
from typing import Annotated


app = FastAPI()
# Dependency with yield 
class OwnerError(Exception):
    pass

def get_username():
    try:
        yield "Atul"
    except OwnerError as e:
        raise HTTPException(status_code=400, detail=f"Owner error: {e}")
    
@app.get("/item/{item_id}")
def get_items(item_id: str, usenname: Annotated[str, Depends(get_username)]):
    data = {
        "pressure-cooker":{"description":"Essential for making food", "owner":"Atul"},
        "scooty": {"description": "Zypy ride for city streats", "owner":"Krishna"} 
    }

    if item_id not in data:
        raise HTTPException(status_code=400, detail="Item not found")
    
    item = data[item_id]
    print(item)
    if item["owner"] != usenname:
        raise OwnerError(usenname)
    
    return item