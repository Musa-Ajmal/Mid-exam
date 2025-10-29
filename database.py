from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base,sessionmaker


import os


DATABASE_URL = os.getenv("DATABASE_URL")

if not DATABASE_URL:
    raise ValueError("No DATABASE_URL set in environment variables")

engine = create_engine(DATABASE_URL)

Base=declarative_base()

Session=sessionmaker()