# About Project
1. Dependancy injection used in this application


# Depends input
1. If you use `Depends()` then input box will not show in swagger. role input box will not be show in swagger

````
@app.get("/admin")
async def admin_only(role: Annotated[int, Depends(user_role)]): 
    return role

````

