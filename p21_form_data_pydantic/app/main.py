from fastapi import FastAPI, Form
from fastapi.responses import HTMLResponse
from typing import Annotated
from pydantic import BaseModel, Field

app = FastAPI()


## A simple html form for testing
## You will see in browser not in swagger documentation
@app.get("/", response_class=HTMLResponse)
async def get_form():
    return """
<html>
   <body>
        <h2>Login Form</h2>
        <form action="/login" method="post">
            <label for="username"> Username: </label><br>
            <input type="text" id="username" name="username"><br>
            <label for="password"> Password: </label><br>
            <input type="password" id="password" name="password"><br>
            <input type="submit" value="Submit">
        </form>
   </body>
</html>

"""

# class FormData(BaseModel):
#     username: str  # same as form input box name attribute value
#     password: str  # same as form input box name attribute value


class FormData(BaseModel):
    username: str = Field(min_length=3) # same as form input box name attribute value
    password: str = Field(min_length=3, max_length=20) # same as form input box name attribute value
    model_config = {"extra":"forbid"} # If extra field comming then it give error

# here will use only form field 
@app.post("/login")
async def login(data: Annotated[FormData,Form()]):
    return data