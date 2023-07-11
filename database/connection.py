import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


username = os.getenv("DB_USERNAME")
password = os.getenv("DB_PASSWORD")
db_name = os.getenv("DB_NAME")
host = "database-1.czynyskp3eco.us-east-2.rds.amazonaws.com"

SQLALCHEMY_DATABASE_URL = f"postgresql://{username}:{password}@{host}/{db_name}"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

