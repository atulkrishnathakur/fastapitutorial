# About project
1. In this project we are using asyncronous way to connect postgresql

# If you want to use syncronous 
```
pip install "fastapi[standard]" sqlalchemy psycopg2-binary
```

# If you want to use asyncronous 
```
pip install "fastapi[standard]" sqlalchemy[asyncio] asyncpg

```

# install the packages
1. install sqlalchemy
```
pip install sqlalchemy[asyncio] 
```
2. install asyncpg
```
pip install asyncpg
```

3. It is used to read data from .env file
```
pip install python-decouple
```