from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtWidgets import QWidget, QLabel, QLineEdit, QComboBox, QDateEdit, QPushButton, QVBoxLayout, QMessageBox
from PyQt5.QtCore import QDate

class RegistrationView(QWidget):
    def __init__(self, controller):
        super().__init__()
        self.controller = controller
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Registration Page")
        self.setGeometry(100, 100, 300, 400)

        # Registration fields
        self.first_name_label = QLabel("First Name:", self)
        self.first_name_input = QLineEdit(self)

        self.last_name_label = QLabel("Last Name:", self)
        self.last_name_input = QLineEdit(self)

        self.dob_label = QLabel("Date of Birth:", self)
        self.dob_input = QDateEdit(self)
        self.dob_input.setDate(QDate.currentDate())

        self.gender_label = QLabel("Gender:", self)
        self.gender_input = QComboBox(self)
        self.gender_input.addItems(["Male", "Female"])

        self.email_label = QLabel("Email:", self)
        self.email_input = QLineEdit(self)

        self.password_label = QLabel("Password:", self)
        self.password_input = QLineEdit(self)
        self.password_input.setEchoMode(QLineEdit.Password)

        self.register_submit_btn = QPushButton("Register", self)
        self.register_submit_btn.clicked.connect(self.handle_register)

        # Layout for registration form
        self.reg_layout = QVBoxLayout()
        self.reg_layout.addWidget(self.first_name_label)
        self.reg_layout.addWidget(self.first_name_input)
        self.reg_layout.addWidget(self.last_name_label)
        self.reg_layout.addWidget(self.last_name_input)
        self.reg_layout.addWidget(self.dob_label)
        self.reg_layout.addWidget(self.dob_input)
        self.reg_layout.addWidget(self.gender_label)
        self.reg_layout.addWidget(self.gender_input)
        self.reg_layout.addWidget(self.email_label)
        self.reg_layout.addWidget(self.email_input)
        self.reg_layout.addWidget(self.password_label)
        self.reg_layout.addWidget(self.password_input)
        self.reg_layout.addWidget(self.register_submit_btn)

        self.setLayout(self.reg_layout)

    def handle_register(self):
        # Get the data from inputs
        first_name = self.first_name_input.text()
        last_name = self.last_name_input.text()
        dob = self.dob_input.date().toString("yyyy-MM-dd")
        gender = self.gender_input.currentText()
        email = self.email_input.text()
        password = self.password_input.text()

        # Pass the data to the controller's register method
        result = self.controller.register(email, password, first_name, last_name, dob, gender)

        # Show the result in a message box
        self.show_message(result)

    def show_message(self, message):
        msg = QMessageBox()
        msg.setWindowTitle("Registration Result")
        msg.setText(str(message))
        msg.exec_()
