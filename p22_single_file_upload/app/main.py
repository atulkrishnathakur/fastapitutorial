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
        <h2>Single File Upload</h2>
        <form action="/file" enctype="multipart/form-data" method="post">
            <input type="file"  name="file"><br>
            <input type="submit" value="Upload">
        </form>

        <h2>Single file upload by using UploadFile </h2>
        <form action="/uploadfile" enctype="multipart/form-data" method="post">
            <input type="file"  name="file"><br>
            <input type="submit" value="Upload">
        </form>
   </body>
</html>

"""


# bytes work well with small size files
# you can not get filename and details if you use bytes
@app.post("/file")
async def uploadfile_by_bytes(file: Annotated[bytes | None,File()] = None):
    if not file:
        return {"message": "No file sent"}
    filename = f"{uuid.uuid4()}.bin" # create a unique file name with .bin extension. You can use other extension as per your need.
    save_path = f"uploads/{filename}" # File save on this path
    os.makedirs("uploads",exist_ok=True) # makedirs create directory if not exist. exist_ok=True will not give error if file already exist and makedirs goes to create file.
    with open(save_path, 'wb') as buffer: # file open in write binary mode
        buffer.write(file) # write data in bin file
    return {"file size": len(file)}


# UploadFile used to upload big file
# 'wb' mode is used when text,images, pdf, zip file uplaod else file can be cruppted.
# If you are going to upload unknown file then 'wb' is better.


@app.post('/uploadfile')
async def uploadfile_by_uploadfile(file: Annotated[UploadFile | None, File()]):
    if not file:
        return {"message":"No upload file sent"}
    clientFileName = file.filename
    contentType = file.content_type
    save_path = f"uploads/{clientFileName}"
    os.makedirs("uploads",exist_ok=True)
    with open(save_path,'wb') as buffer:
        shutil.copyfileobj(file.file,buffer)
    
    return {"filename":clientFileName,"content_type":contentType}
