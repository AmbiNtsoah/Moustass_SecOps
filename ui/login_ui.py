from PyQt5.QtWidgets import (
    QWidget,
    QLabel,
    QLineEdit,
    QPushButton,
    QVBoxLayout,
    QMessageBox
)
from PyQt5.QtCore import Qt

from ui.first_password_dialog import FirstPasswordDialog


class LoginWindow(QWidget):
    """Fenêtre de login. Délègue la logique à AuthService."""

    def __init__(self, auth_service):
        print(">>> LoginWindow __init__ appelée")   
        super().__init__()
        self.auth_service = auth_service
        self.setWindowTitle("Login")
        self.setFixedSize(360, 180)
        self._build_ui()

    def _build_ui(self):
        self.email_input = QLineEdit()
        self.email_input.setPlaceholderText("Email")

        self.password_input = QLineEdit()
        self.password_input.setEchoMode(QLineEdit.Password)
        self.password_input.setPlaceholderText("Password")

        login_btn = QPushButton("Login")
        login_btn.clicked.connect(self._on_login_clicked)

        layout = QVBoxLayout()
        layout.addWidget(QLabel("<h2>Connexion</h2>"), alignment=Qt.AlignCenter)
        layout.addWidget(self.email_input)
        layout.addWidget(self.password_input)
        layout.addWidget(login_btn)

        self.setLayout(layout)

    def _on_login_clicked(self):
        email = self.email_input.text().strip()
        password = self.password_input.text().strip()

        if not email or not password:
            QMessageBox.warning(self, "Erreur", "Remplissez tous les champs")
            return

        success, message, user = self.auth_service.authenticate(email, password)
        if not success:
            QMessageBox.critical(self, "Erreur", message)
            return

        # si first_login -> forcer changement de mot de passe
        if user.get("is_first_password", 0) == 1:
            dlg = FirstPasswordDialog(user=user, auth_service=self.auth_service)
            if dlg.exec_() == dlg.Accepted:
                QMessageBox.information(self, "OK", "Mot de passe mis à jour. Connecté.")
                self.open_main_window(user)
            else:
                QMessageBox.information(self, "Info", "Vous devez changer votre mot de passe pour continuer.")
                # return
        else:
            QMessageBox.information(self, "OK", "Connexion réussie.")
            self.open_main_window(user)

    def open_main_window(self, user):
        """
        Exemple minimal : si user.role == 'admin' ouvrir l'UI admin de création.
        Ici on ouvre la fenêtre admin (si admin) sinon on ferme et continue.
        """
        if user.get("role") == "admin":
            from ui.admin_create_user import AdminCreateUserWindow
            admin_win = AdminCreateUserWindow(self.auth_service)
            admin_win.show()