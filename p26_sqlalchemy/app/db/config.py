from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import os 

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
db_path = os.path.join(BASE_DIR,"sqlite.db")

# echo=True used to print sql query in terminal. it is usefull for debugging.

DATABASEURL = f"sqlite:///{db_path}"
engin = create_engine(DATABASEURL, echo=True)
SessionLocal = sessionmaker(bind=engin, expire_on_commit=False)