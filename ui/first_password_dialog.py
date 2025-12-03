from PyQt5.QtWidgets import QDialog, QVBoxLayout, QLineEdit, QPushButton, QMessageBox


class FirstPasswordDialog(QDialog):
    """Dialogue pour forcer le changement du mot de passe au premier login."""

    def __init__(self, user: dict, auth_service):
        super().__init__()
        self.user = user
        self.auth_service = auth_service
        self.setWindowTitle("Changer le mot de passe (1er login)")
        self.setFixedSize(360, 140)
        self._build_ui()

    def _build_ui(self):
        self.new_pwd = QLineEdit()
        self.new_pwd.setEchoMode(QLineEdit.Password)
        self.new_pwd.setPlaceholderText("Nouveau mot de passe")

        self.confirm_pwd = QLineEdit()
        self.confirm_pwd.setEchoMode(QLineEdit.Password)
        self.confirm_pwd.setPlaceholderText("Confirmer le mot de passe")

        btn = QPushButton("Valider")
        btn.clicked.connect(self._on_validate)

        layout = QVBoxLayout()
        layout.addWidget(self.new_pwd)
        layout.addWidget(self.confirm_pwd)
        layout.addWidget(btn)
        self.setLayout(layout)

    def _on_validate(self):
        p1 = self.new_pwd.text().strip()
        p2 = self.confirm_pwd.text().strip()
        if not p1 or not p2:
            QMessageBox.warning(self, "Erreur", "Remplissez les deux champs.")
            return
        if p1 != p2:
            QMessageBox.warning(self, "Erreur", "Les mots de passe ne correspondent pas.")
            return
        if len(p1) < 6:
            QMessageBox.warning(self, "Erreur", "Mot de passe trop court (min 6 caractères).")
            return

        # Appel du service pour mettre à jour et désactiver le flag first_password
        self.auth_service.change_password_first_time(self.user["idusers"], p1)
        QMessageBox.information(self, "OK", "Mot de passe changé.")
        self.accept()
