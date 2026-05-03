# About project
1. In this project we are using asyncronous way to connect mysql

# If you want to use syncronous 
```
pip install "fastapi[standard]" sqlalchemy pymysql
```

# If you want to use asyncronous 
```
pip install "fastapi[standard]" sqlalchemy[asyncio] aiomysql

```

# install the packages
1. install sqlalchemy
```
pip install sqlalchemy[asyncio] 
```
2. install aiomysql
```
pip install aiomysql
```

3. It is used to read data from .env file
```
pip install python-decouple
```