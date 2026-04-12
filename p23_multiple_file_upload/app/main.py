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
        <form action="/uploadfiles" enctype="multipart/form-data" method="post">
            <input type="file"  name="files" multiple><br>
            <input type="submit" value="Upload">
        </form>
   </body>
</html>
"""


@app.post('/uploadfiles')
async def uploadfile_by_uploadfile(files: Annotated[list[UploadFile], File()]):
    save_files = []
    os.makedirs("uploads",exist_ok=True)
    for file in files:
        save_path = f"uploads/{file.filename}"
        with open(save_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)
        save_files.append({"filename": file.filename})
    return save_files