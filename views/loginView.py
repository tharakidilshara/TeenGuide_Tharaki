from PyQt5.QtWidgets import QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QMessageBox
from views.registrationView import RegistrationView  # Make sure the path is correct

class LoginView(QWidget):
    def __init__(self, controller):
        super().__init__()
        self.controller = controller
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Login Page")
        self.setGeometry(100, 100, 300, 300)

        # Login fields
        self.email_label = QLabel("Email:", self)
        self.email_input = QLineEdit(self)

        self.password_label = QLabel("Password:", self)
        self.password_input = QLineEdit(self)
        self.password_input.setEchoMode(QLineEdit.Password)

        self.login_btn = QPushButton("Login", self)
        self.login_btn.clicked.connect(self.handle_login)

        self.register_btn = QPushButton("Register", self)
        self.register_btn.clicked.connect(self.show_register_form)

        # Layout for login form
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.email_label)
        self.layout.addWidget(self.email_input)
        self.layout.addWidget(self.password_label)
        self.layout.addWidget(self.password_input)
        self.layout.addWidget(self.login_btn)
        self.layout.addWidget(self.register_btn)

        self.setLayout(self.layout)

    def handle_login(self):
        email = self.email_input.text()
        password = self.password_input.text()
        result = self.controller.login(email, password)
        self.show_message(result)

    def show_register_form(self):
        # Hide the current login window and show the registration window
        self.hide()  # This hides the login form
        self.registration_view = RegistrationView(self.controller)
        self.registration_view.show()  # This opens the registration form

    def show_message(self, message):
        msg = QMessageBox()
        msg.setWindowTitle("Result")
        msg.setText(str(message))
        msg.exec_()
