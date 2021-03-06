import pandas as pd
import os
import sys
if os.getenv('MY_PYTHON_PKG') not in sys.path:
    sys.path.append(os.getenv('MY_PYTHON_PKG'))
import syspath

SQLITE_DB = os.getenv('SQLITE_DB')

PG_HOST = os.getenv('PG_HOST')
MONGO_HOST = os.getenv('MONGO_HOST')

PG_PWD = os.getenv('PG_DOCKER_PWD')
MYSQL_PWD = os.getenv('MYSQL_PWD')
MONGO_PWD = os.getenv('MONGO_DOCKER_PWD')

PG_PORT = int(os.getenv('PG_DOCKER_PORT'))
MYSQL_PORT = int(os.getenv('MYSQL_PORT'))
MONGO_PORT = int(os.getenv('MONGO_DOCKER_PORT'))

PG_USER = os.getenv('PG_DOCKER_USER')
MYSQL_USER = os.getenv('MYSQL_USER')
MONGO_USER = os.getenv('MONGO_DOCKER_USER')

pd.get_option("display.max_rows")
pd.get_option("display.max_columns")
pd.set_option("display.max_rows", 100)
pd.set_option("display.max_columns", 1000)
pd.set_option('display.expand_frame_repr', False)
pd.set_option('display.unicode.east_asian_width', True)
