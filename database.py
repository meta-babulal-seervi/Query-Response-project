from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker , declarative_base
from dotenv import load_dotenv
import os

load_dotenv()  # Loads from .env by default

# Now you can access the variables
database_url = os.getenv("DATABASE_URL")



SQLALCHEMY_DATABASE_URL = database_url

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit = False , autoflush = False , bind = engine)
Base = declarative_base()