#This file will load the data using the psycopg2 driver
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

#databaseURL = f"postgresql://{user}:{passwd}@{host}:{port}/{database}"

#In order to retry the connection before the server starts the while loop is used
while True:
    try:
        conn = psycopg2.connect(host=host,
                        dbname=database,user=user,
                        password=passwd,port=port,
                            cursor_factory=RealDictCursor)

        conn.set_session(autocommit=True)

        cur = conn.cursor()
        print("connection established...")
        break

    except Exception as e:
        print(e)
        time.sleep(2)

#Initiating the table loading routine
target_query = input("please provide the full query to load the data: ")

def load_data(query: str):
    print("The query executed is",query)
    cur.execute(query)

load_data(target_query)

