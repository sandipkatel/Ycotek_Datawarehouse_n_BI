# ./
##import constants

import snowflake.connector
import logging
from lib.Variables import Variables
from lib.Logger import Logger
v=Variables()

USER = v.get("user")
PASSWORD = v.get("password")
ACCOUNT = v.get("account")
DATABASE = v.get("database")
SCHEMA = v.get("schema")
DATA_WAREHOUSE = v.get("warehouse")


ctx = snowflake.connector.connect(
    user= USER,
    password=PASSWORD,
    account=ACCOUNT,
    database=DATABASE,
    schema=SCHEMA
    )

cs = ctx.cursor()



def execute_query(query):
    try:
        cs.execute(f"USE WAREHOUSE {DATA_WAREHOUSE}")
        cs.execute(query)
        print(cs.fetchall())
        Logger.log_message(f"query executed: {query}")
    except Exception as e:
        print(e, query)
        Logger.log_message(f"query error: {query}")
        Logger.log_message(e)
    # finally:
    #     cs.close()
    # ctx.close()

def executemany(query, params):
    try:
        cs.execute(f"USE WAREHOUSE {DATA_WAREHOUSE}")
        cs.executemany(query, params)
        # print(cs.fetchall())
        Logger.log_message(f"query executed: {query}")
    except Exception as e:
        print(e, query)
        Logger.log_message(f"query error: {query}")
        Logger.log_message(e)
    # finally:
    #     cs.close()
    # ctx.close()


def fetch_data(query):
    try:
        cs.execute(f"USE WAREHOUSE {DATA_WAREHOUSE}")
        cs.execute(query)
        Logger.log_message(f"query executed: {query}")
        return cs.fetchall()
    except Exception as e:
        print(e, query)
        Logger.log_message(f"query error: {query}")
        Logger.log_message(e)

execute_query("USE DATABASE IOE")
fetch_data("SHOW TABLES IN SCHEMA PUBLIC")