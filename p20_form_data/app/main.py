from fastapi import FastAPI, Form
from fastapi.responses import HTMLResponse
from typing import Annotated


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


# here username and password in form field name attribute value
# here will use only form field 
@app.post("/login")
async def login(
    username: Annotated[str,Form(min_length=3)],
    password: Annotated[str,Form(min_length=3, max_length=20)]
    ):
    return {"username": username, "passord_length": len(password)}