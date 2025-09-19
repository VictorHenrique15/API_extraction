import psycopg2
from dotenv import load_dotenv
import os

conn = psycopg2.connect(
    dbname='DB_NAME',
    user='DB_USER',
    password='DB_PASSWORD',
    host='DB_HOST',
    port='DB_PORT'
)
