import configparser
import utilities
from api_testing import *
import mysql.connector.connection
from mysql.connector.connection import *
from api_testing.payload import newdata
def config():
    config = configparser.ConfigParser()
    config.read("C:\\Users\\akash\\PycharmProjects\\Practicepython\\utilities\\prop.ini")
    return config
connect = {"user": config()["SQL"]['user'],"password": config()['SQL']['password'],"database": config()['SQL']['database'],"host": config()['SQL']['host']}
def connection():
    conn= mysql.connector.connect(**connect)
    return conn
def getquery(query):
    conn= connection()
    cursor =conn.cursor()
    cursor.execute(query)
    row = cursor.fetchone()
    conn.close()
    return row