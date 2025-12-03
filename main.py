print("import DB_CONFIG")
from config.database_config import DB_CONFIG
print("import DbConnector")
from db.connector_db import DbConnector
print("import UserDAO")
from ui.user_dao import UserDAO
print("import AuthService")
from controllers.auth_controller import AuthService
print("import LoginWindow")
from ui.login_ui import LoginWindow
import sys
from PyQt5.QtWidgets import QApplication


print(">>> TOUS LES IMPORTS SONT OK")

def main():
    # Init DB
    db = DbConnector(DB_CONFIG)
    db.connect()

    # DAO + Services
    user_dao = UserDAO(db)
    auth_service = AuthService(user_dao)

    # App
    app = QApplication(sys.argv)
    login = LoginWindow(auth_service)
    login.show()
    result = app.exec_()

    # Cleanup
    db.close()
    sys.exit(result)


if __name__ == "__main__":
    print(">>> Début du programme")
    main()