
# configure vs code editor for python/fastapi development
1. install vs code and install `python` extension of vs code

# how to select interpretor in vs code
1. press `Ctrl + Shift + p` then choose `Select: Python Interpreter`
2. Then choose `Enter interpreter path` then go `venv/bin` and choose `python3.14`

# run fastapi as development mode
```
(venv) atulkrishnathakur@atul-pc:~/fastapitutorial/p2$ fastapi dev main.py
```
or
```
(venv) atulkrishnathakur@atul-pc:~/fastapitutorial/p2$ uvicorn main:app --reload
```
- press ctrl+c to quit



# Handle Form data
- Some time you have need to send form data in API instead of JSON formate in response.

