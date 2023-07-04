import psycopg2
from flask import Flask 
import logging
logging.basicConfig(level=logging.DEBUG)

app = Flask(__name__)
#pp.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres@localhost:5432/bank'


def connection():
    conn = psycopg2.connect("dbname=bank user=postgres host=localhost port=5432")
    conn.set_session(autocommit=True)
    return conn

