from fastapi.testclient import TestClient
import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

from server.main import playserver 

from server.dbengine import get_db
from server.dbengine import Base
from server import db_model
from alembic import command

import psycopg2
from psycopg2.extras import RealDictCursor
import configparser

creden = configparser.ConfigParser()
creden.read_file(open('calter.config'))
host = creden["LOCALPG"]["PG_HOST"]
database = creden["LOCALPG"]["PG_DB_FAST"] 
port = creden["LOCALPG"]["PG_PORT"]
passwd = creden["LOCALPG"]["PG_PASS"]
user = creden["LOCALPG"]["PG_UNAME"]

#In order to retry the connection before the server starts the while loop is used
while True:
    try:
        conn = psycopg2.connect(host=host,
                        dbname='fastapi_test',user=user,
                        password=passwd,port=port,
                            cursor_factory=RealDictCursor)

        conn.set_session(autocommit=True)

        cur = conn.cursor()
        print("connection established...")
        break

    except Exception as e:
        print(e)
        time.sleep(2)


def load_data(query: str):
    print("The query executed is",query)
    cur.execute(query)

def query_data():
    print("Querying the database, and printing the output")
    cur.execute("""SELECT * FROM google_merchandise LIMIT 1""")
    query_out= cur.fetchone()
    print(query_out)

# SQLALCHEMY_DATABASE_URL = 'postgresql://postgres:password123@localhost:5432/fastapi_test'
SQLALCHEMY_DATABASE_URL = f'postgresql://{user}:{passwd}@{host}:{port}/{database}_test'

engine = create_engine(SQLALCHEMY_DATABASE_URL)

TestingSessionLocal = sessionmaker(
    autocommit=False, autoflush=False, bind=engine)


@pytest.fixture()
def session():
    print("my session fixture ran")
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)
    print("new binding created")
    load_data("""copy google_merchandise(categories,price,timeDate) 
              FROM '/run/media/solverbot/repoA/gitFolders/rilldash/googleMerchPurchases.csv' 
              WITH CSV HEADER DELIMITER ',';""")
    query_data()
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()


@pytest.fixture()
def client(session):
    def override_get_db():

        try:
            yield session
        finally:
            session.close()
    playserver.dependency_overrides[get_db] = override_get_db
    yield TestClient(playserver)
