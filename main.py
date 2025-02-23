import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from PyQt5.QtWidgets import QApplication
from controllers.loginController import LoginController
from views.loginView import LoginView

if __name__ == "__main__":
    app = QApplication(sys.argv)
    controller = LoginController()
    view = LoginView(controller)
    view.show()
    sys.exit(app.exec_())
