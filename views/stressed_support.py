
import os
import random
from PyQt5.QtWidgets import (
    QMainWindow, QWidget, QLabel, QPushButton,
    QVBoxLayout, QMessageBox, QLineEdit
)

# Ensure the correct directory for messages
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MESSAGES_FOLDER = os.path.join(BASE_DIR, "messages")


class MoodRatingWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Mood Rating")
        self.setGeometry(400, 200, 400, 300)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout()

        self.label_question = QLabel("Rate your mood on a scale of 1 to 10:")
        self.layout.addWidget(self.label_question)

        self.rating_buttons = []
        for i in range(1, 11):
            btn = QPushButton(str(i))
            btn.clicked.connect(lambda checked, value=i: self.select_rating(value))
            self.layout.addWidget(btn)
            self.rating_buttons.append(btn)

        self.btn_quit = QPushButton("❌ Quit")
        self.btn_quit.clicked.connect(self.close)
        self.layout.addWidget(self.btn_quit)

        self.central_widget.setLayout(self.layout)

    def select_rating(self, value):
        self.close()
        self.issue_selection_window = IssueSelectionWindow(value)
        self.issue_selection_window.show()


class IssueSelectionWindow(QMainWindow):
    def __init__(self, mood_rating):
        super().__init__()
        self.mood_rating = mood_rating
        self.setWindowTitle("Select Your Issue")
        self.setGeometry(400, 200, 400, 300)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout()

        self.label_question = QLabel(f"You rated your mood as {mood_rating}/10. What is your issue?")
        self.layout.addWidget(self.label_question)

        issues = {
            "School Bully": self.open_chat,
            "Financial Issues": lambda: self.show_help("financial"),
            "Social Crises": lambda: self.show_help("social"),
            "Health Issues": lambda: self.show_help("health"),
            "Family Issues": lambda: self.show_help("family"),
        }

        for issue, action in issues.items():
            btn = QPushButton(issue)
            btn.clicked.connect(action)
            self.layout.addWidget(btn)

        self.btn_back = QPushButton("← Back")
        self.btn_back.clicked.connect(self.go_back)
        self.layout.addWidget(self.btn_back)

        self.btn_quit = QPushButton("❌ Quit")
        self.btn_quit.clicked.connect(self.close)
        self.layout.addWidget(self.btn_quit)

        self.central_widget.setLayout(self.layout)

    def show_help(self, issue_type):
        self.close()
        self.help_window = HelpWindow(issue_type)
        self.help_window.show()

    def open_chat(self):
        self.close()
        self.chat_window = ChatBotWindow()
        self.chat_window.show()

    def go_back(self):
        self.close()
        self.mood_rating_window = MoodRatingWindow()
        self.mood_rating_window.show()


class HelpWindow(QMainWindow):
    def __init__(self, issue_type):
        super().__init__()
        self.setWindowTitle("Help Resources")
        self.setGeometry(400, 200, 400, 300)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout()

        help_messages = {
            "financial": "💰 Here are job websites:\n\n• Indeed: https://www.indeed.com\n• LinkedIn Jobs: https://www.linkedin.com/jobs\n\nBest of luck for the future!",
            "social": "🌍 Social help links:\n\n• Crisis Text Line: https://www.crisistextline.org\n• Mental Health Support: https://www.nami.org\n\nYou're not alone!",
            "health": "🏥 Health services:\n\n• Emergency: Dial 911\n• Mental Health Hotline: 1-800-662-HELP\n\nTake care!",
            "family": "👨‍👩‍👦 Family Support:\n\n• National Parent Helpline: 1-855-427-2736\n\nStay strong!"
        }

        self.label_info = QLabel(help_messages.get(issue_type, "No information available."))
        self.layout.addWidget(self.label_info)

        self.btn_back = QPushButton("← Back")
        self.btn_back.clicked.connect(self.go_back)
        self.layout.addWidget(self.btn_back)

        self.btn_quit = QPushButton("❌ Quit")
        self.btn_quit.clicked.connect(self.close)
        self.layout.addWidget(self.btn_quit)

        self.central_widget.setLayout(self.layout)

    def go_back(self):
        self.close()
        self.issue_selection_window = IssueSelectionWindow(5)
        self.issue_selection_window.show()


class ChatBotWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("ChatBot - School Bullying Support")
        self.setGeometry(400, 200, 400, 300)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout()

        self.label_chat = QLabel("👋 How may I help you?")
        self.layout.addWidget(self.label_chat)

        self.input_box = QLineEdit()
        self.layout.addWidget(self.input_box)

        self.btn_send = QPushButton("Send")
        self.btn_send.clicked.connect(self.get_response)
        self.layout.addWidget(self.btn_send)

        self.chat_responses = [
            "You're not alone! Have you spoken to a trusted teacher or parent?",
            "Bullying is serious. Consider reporting it to school authorities.",
            "Stay confident and surround yourself with positive friends.",
            "Would you like resources to stop bullying? Check: https://www.stopbullying.gov",
            "Take care of yourself. You deserve respect!"
        ]

        self.btn_back = QPushButton("← Back")
        self.btn_back.clicked.connect(self.go_back)
        self.layout.addWidget(self.btn_back)

        self.btn_quit = QPushButton("❌ Quit")
        self.btn_quit.clicked.connect(self.close)
        self.layout.addWidget(self.btn_quit)

        self.central_widget.setLayout(self.layout)

    def get_response(self):
        user_input = self.input_box.text()
        if user_input:
            response = random.choice(self.chat_responses)
            QMessageBox.information(self, "ChatBot", response)
            self.input_box.clear()

    def go_back(self):
        self.close()
        self.issue_selection_window = IssueSelectionWindow(5)
        self.issue_selection_window.show()
 
 
# Ensure this only runs if this file is executed directly

if __name__ == "__main__":
    import sys
    from PyQt5.QtWidgets import QApplication

    app = QApplication(sys.argv)
    window = MoodRatingWindow()
    window.show()
    sys.exit(app.exec_())