#This file connects the server to the database
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

import configparser

cred = configparser.ConfigParser()
cred.read_file(open('calter.config'))

host = cred["LOCALPG"]["PG_HOST"]
db_name = cred["LOCALPG"]["PG_DB_FAST"]
port = cred["LOCALPG"]["PG_PORT"]
passwd = cred["LOCALPG"]["PG_PASS"]
user = cred["LOCALPG"]["PG_UNAME"]

sqlalchemy_url = f"postgresql://{user}:{passwd}@{host}:{port}/{db_name}"

engine = create_engine(sqlalchemy_url)

SessionLocal = sessionmaker(autocommit=False,
                            autoflush=False,
                            bind=engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
