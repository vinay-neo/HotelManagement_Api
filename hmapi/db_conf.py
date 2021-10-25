import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session,sessionmaker


load_dotenv(".env")

# configure the db
SQLALCHEMY_DATABASE_URL = os.environ.get("DATABASE_URL")

#  create engine instance
engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
)

db_session = scoped_session(sessionmaker(autocommit=False,autoflush=False, bind=engine))
db= db_session.session_factory()
Base = declarative_base()
Base.query = db_session.query_property()

def get_db():
    db = db_session()
    try:
        yield db
    finally:
        db.close()

    