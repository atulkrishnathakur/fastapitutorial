from fastapi import FastAPI, Form, File, UploadFile
from fastapi.responses import HTMLResponse
from typing import Annotated
from pydantic import BaseModel, Field
import os
import uuid
import shutil # python built-in package

app = FastAPI()


## A simple html form for testing
## You will see in browser not in swagger documentation
@app.get("/", response_class=HTMLResponse)
async def get_form():
    return """
<html>
   <body>
        <h2>Multiple file upload by using UploadFile </h2>
        <form action="/save" enctype="multipart/form-data" method="post">
            <label for="username">Username:</label>
            <input type="text" id="username" name="username" required><br><br>
            <input type="file"  name="file" id="file"><br>
            <input type="submit" value="Save">
        </form>
   </body>
</html>
"""


@app.post('/save')
async def save(
    username: Annotated[str, Form()],
    file: Annotated[UploadFile | None, File()] = None
):
    response = {"username": username}
    if file:
        save_path = f"uploads/{file.filename}"
        os.makedirs("uploads",exist_ok=True)
        with open(save_path, "wb") as buffer:
            shutil.copyfileobj(file.file,buffer)
        response["filename"] = file.filename
    return response