"""
User Data Access Object — responsable uniquement des opérations SQL liées aux users.
"""
from typing import Optional, Dict, Any


class UserDAO:
    """DAO pour la table users."""

    def __init__(self, db: "DbConnector"):
        self.db = db

    def get_user_by_email(self, email: str) -> Optional[Dict[str, Any]]:
        """Retourne un dictionnaire utilisateur ou None."""
        cursor = self.db.connexion.cursor(dictionary=True)
        cursor.execute("SELECT * FROM users WHERE email = %s", (email,))
        user = cursor.fetchone()
        cursor.close()
        return user

    def get_user_by_id(self, user_id: int) -> Optional[Dict[str, Any]]:
        cursor = self.db.connexion.cursor(dictionary=True)
        cursor.execute("SELECT * FROM users WHERE idusers = %s", (user_id,))
        user = cursor.fetchone()
        cursor.close()
        return user

    def create_user(self, name: str, email: str, role: str, password_hash: str) -> int:
        """Crée un utilisateur. Retourne l'id inséré."""
        cursor = self.db.connexion.cursor()
        query = """
            INSERT INTO users (name, email, role, password_hash, is_first_password)
            VALUES (%s, %s, %s, %s, %s)
        """
        cursor.execute(query, (name, email, role, password_hash, 1))
        self.db.connexion.commit()
        user_id = cursor.lastrowid
        cursor.close()
        return user_id

    def update_password(self, user_id: int, password_hash: str) -> None:
        """Met à jour le mot de passe et déchoque le flag first password."""
        cursor = self.db.connexion.cursor()
        query = "UPDATE users SET password_hash = %s, is_first_password = 0 WHERE idusers = %s"
        cursor.execute(query, (password_hash, user_id))
        self.db.connexion.commit()
        cursor.close()
