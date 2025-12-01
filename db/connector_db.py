""" This file is going to link our software with our DB"""
from mysql.connector import connect, errorcode
from dotenv import load_dotenv
import mysql.connector
import os

load_dotenv()

class DbConnector():
    """ Constructor of our class"""
    def __init__(self):
        self.config = {
            'host': os.getenv("DB_HOST"),
            'user': os.getenv("DB_USER"),
            'password': os.getenv("DB_PASSWORD"),
            'database': os.getenv("DB_DATABASE"),
        }
        self.connexion = None

    def connect(self):
        try :
            self.connexion = mysql.connector.connect(**self.config)
            print("DB Connected successfully !")
        except mysql.connector.Error as error:
            if error.errno == errorcode.ER_ACCESS_DENIED_ERROR :
                raise RuntimeError ("Wrong connecting information ")
            elif error.errno == errorcode.ER_BAD_DB_ERROR :
                raise RuntimeError ("wrong Database")
            else :
                raise
    print("==== END OF connector_db ====")
