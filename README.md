
# About this project
1. Every "p*" is a project for a fastapi topic, chapter or concept

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



# SQLAlchemy installation
1. https://docs.sqlalchemy.org/en/20/intro.html#installation


# install alembic
1. https://alembic.sqlalchemy.org/en/latest/
2. https://alembic.sqlalchemy.org/en/latest/cookbook.html
3. https://alembic.sqlalchemy.org/en/latest/front.html 


# alembic with async 
1. https://alembic.sqlalchemy.org/en/latest/
2. https://alembic.sqlalchemy.org/en/latest/front.html
3. install alembic 
```
(venv) atulkrishnathakur@atul-pc:~/fastapitutorial/p27_async_sqlalchemy$ pip install alembic
```
4. https://alembic.sqlalchemy.org/en/latest/cookbook.html
```
(venv) atulkrishnathakur@atul-pc:~/fastapitutorial/p27_async_sqlalchemy$ alembic init -t async alembic
```

5. in `alembic/env.py` file write the `render_as_batch=True`. Note it is only use for sqlite
```
def do_run_migrations(connection: Connection) -> None:
    context.configure(
        connection=connection,
        target_metadata=target_metadata,
        render_as_batch=True
        )

```

# install async sqlalchemy
1. ref: https://docs.sqlalchemy.org/en/20/orm/extensions/index.html
2. Ref: https://docs.sqlalchemy.org/en/20/orm/extensions/asyncio.html 

# SQLite for Async support
1. SQLite does not support async so first need to install 
```
$ pip install aiosqlite
```