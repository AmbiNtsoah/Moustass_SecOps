"""
Db connector module — responsable uniquement de la connexion à la base.
"""
import mysql.connector
from mysql.connector import errorcode


class DbConnector:
    """Gère la connexion MySQL."""

    def __init__(self, config: dict):
        self.config = config
        self.connexion = None

    def connect(self) -> None:
        """Établit la connexion avec la base de données."""
        try:
            self.connexion = mysql.connector.connect(**self.config)
            # Optionnel: set autocommit selon votre besoin
            # self.connexion.autocommit = False
        except mysql.connector.Error as error:
            if error.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                raise RuntimeError("Wrong DB credentials") from error
            if error.errno == errorcode.ER_BAD_DB_ERROR:
                raise RuntimeError("Database does not exist") from error
            raise

    def close(self) -> None:
        """Ferme la connexion si ouverte."""
        if self.connexion and self.connexion.is_connected():
            self.connexion.close()
            self.connexion = None
