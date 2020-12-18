import os
import mysql.connector
from datetime import datetime

database = mysql.connector.connect(
    host="mysql-service",
    user="root",
    password=os.environ.get("MYSQL_ROOT_PASSWORD"),
    database=os.environ.get("MYSQL_DATABASE"),
)

database.close()