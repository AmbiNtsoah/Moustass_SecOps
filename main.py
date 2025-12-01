""" Simple debut Main """
from db.connector_db import DbConnector

def main():
    greet = "Hello Python!"
    print(greet)

if __name__ == "__main__":
    db = DbConnector()
    main()