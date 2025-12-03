"""
Auth service — contient logique d'authentification.
Utilise bcrypt pour le hachage/verification.
"""
import bcrypt
from typing import Tuple, Optional

from ui.user_dao import UserDAO


class AuthService:
    """Service responsable de l'authentification et création d'utilisateur par admin."""

    def __init__(self, user_dao: UserDAO):
        self.user_dao = user_dao

    def authenticate(self, email: str, password: str) -> Tuple[bool, str, Optional[dict]]:
        """
        Vérifie les credentials.
        Retour: (success, message, user_dict_or_None)
        """
        user = self.user_dao.get_user_by_email(email)
        if user is None:
            return False, "Utilisateur introuvable", None

        stored_hash = user["password_hash"].encode("utf-8")
        if not bcrypt.checkpw(password.encode("utf-8"), stored_hash):
            return False, "Mot de passe incorrect", None

        return True, "Authentification réussie", user

    def create_user_by_admin(self, name: str, email: str, role: str, password: str) -> int:
        """Crée un nouvel utilisateur avec mot de passe fourni (provisoire) et flag first_password=1."""
        pw_hash = bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt()).decode("utf-8")
        user_id = self.user_dao.create_user(name=name, email=email, role=role, password_hash=pw_hash)
        return user_id

    def change_password_first_time(self, user_id: int, new_password: str) -> None:
        pw_hash = bcrypt.hashpw(new_password.encode("utf-8"), bcrypt.gensalt()).decode("utf-8")
        self.user_dao.update_password(user_id=user_id, password_hash=pw_hash)
