from PyQt5.QtWidgets import (
    QWidget, QVBoxLayout, QLineEdit, QPushButton, QMessageBox, QLabel
)


class AdminCreateUserWindow(QWidget):
    """UI simple pour que l'admin crée un nouvel utilisateur (provisoire)."""

    def __init__(self, auth_service):
        super().__init__()
        self.auth_service = auth_service
        self.setWindowTitle("Admin - Créer utilisateur")
        self.setFixedSize(400, 260)
        self._build_ui()

    def _build_ui(self):
        self.name_input = QLineEdit()
        self.name_input.setPlaceholderText("Nom complet")

        self.email_input = QLineEdit()
        self.email_input.setPlaceholderText("Email")

        self.role_input = QLineEdit()
        self.role_input.setPlaceholderText("Role (admin/user)")

        self.password_input = QLineEdit()
        self.password_input.setPlaceholderText("Mot de passe provisoire")
        self.password_input.setEchoMode(QLineEdit.Password)

        create_btn = QPushButton("Créer utilisateur")
        create_btn.clicked.connect(self._on_create)

        layout = QVBoxLayout()
        layout.addWidget(QLabel("<h3>Créer un utilisateur</h3>"))
        layout.addWidget(self.name_input)
        layout.addWidget(self.email_input)
        layout.addWidget(self.role_input)
        layout.addWidget(self.password_input)
        layout.addWidget(create_btn)
        self.setLayout(layout)

    def _on_create(self):
        name = self.name_input.text().strip()
        email = self.email_input.text().strip()
        role = self.role_input.text().strip() or "user"
        password = self.password_input.text().strip()

        if not name or not email or not password:
            QMessageBox.warning(self, "Erreur", "Remplissez tous les champs.")
            return

        # Appel au service
        try:
            user_id = self.auth_service.create_user_by_admin(name, email, role, password)
        except Exception as exc:
            QMessageBox.critical(self, "Erreur", f"Impossible de créer l'utilisateur: {exc}")
            return

        QMessageBox.information(self, "OK", f"Utilisateur créé (id: {user_id}). Il devra changer son mot de passe au 1er login.")
        # Option: clear fields
        self.name_input.clear()
        self.email_input.clear()
        self.role_input.clear()
        self.password_input.clear()
