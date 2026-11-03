from fastapi import FastAPI


app = FastAPI()

'''
URL for async and await: https://fastapi.tiangolo.com/async/

'''

'''
If you are using third party libraries that tell you to call them with await, like:


results = await some_library()
Then, declare your path operation functions with async def like:


@app.get("/")
async def read_results():
    results = await some_library()
    return results


'''

'''
If you are using a third party library that communicates with something (a database, an API, the file system, etc.) and doesn't have support for using await, (this is currently the case for most database libraries), then declare your path operation functions as normally, with just def, like:

@app.get("/")
def results():
    results = some_library()
    return results

'''

@app.get('/')
def home():
    return {"message":"hello fastapi"}
