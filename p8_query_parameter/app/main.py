from fastapi import FastAPI

app = FastAPI()


#single query parameter

@app.get("/product")
async def product(category:str, limit:int, country:str = "India", state: str | None = None): 
    '''
    country: default paramenter
    state: optional parameter
    '''
    return {
        "status":"Ok",
        "category":category,
        "limit":limit,
        "country":country
        }


# query and path parameter
@app.get("/product/{year}")
async def product_details(year:int,category:str, limit:int, country:str = "India", state: str | None = None): 
    """
    category: required pareameter
    country: default paramenter
    state: optional parameter
    year:path parameter
    """
    return {
        "status":"Ok",
        "category":category,
        "limit":limit,
        "country":country
        }