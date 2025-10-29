import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from main import app
import os

@pytest.fixture(scope="session")
def db_engine():
    database_url = os.getenv("DATABASE_URL")
    engine = create_engine(database_url)
    yield engine
    engine.dispose()

@pytest.fixture(scope="function")
def db_session(db_engine):
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=db_engine)
    session = SessionLocal()
    yield session
    session.close()

@pytest.fixture(scope="module")
def client():
    with TestClient(app) as c:
        yield c
