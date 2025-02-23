import sys
import os
import random
import stressed_support

from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QLabel, QPushButton,
    QRadioButton, QVBoxLayout, QMessageBox
)
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5.QtCore import QUrl

# Get the absolute path of the current script's directory
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Set absolute paths for music and messages folders
MUSIC_FOLDER = os.path.join(BASE_DIR, "music")
MESSAGES_FOLDER = os.path.join(BASE_DIR, "messages")


class MoodTracker(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Teen Health Care - Mood Tracker")
        self.setGeometry(400, 200, 400, 300)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout()

        # Question 1: "How was your day today?"
        self.label_day_question = QLabel("How was your day today?")
        self.layout.addWidget(self.label_day_question)

        # Question 2: "Are you happy or stressed?"
        self.label_mood_question = QLabel("Are you happy or stressed?")
        self.layout.addWidget(self.label_mood_question)

        self.radio_happy = QRadioButton("Happy 😊")
        self.radio_stressed = QRadioButton("Stressed 😔")
        self.layout.addWidget(self.radio_happy)
        self.layout.addWidget(self.radio_stressed)

        # Navigation Buttons
        self.btn_next = QPushButton("Next →")
        self.btn_next.clicked.connect(self.handle_mood_selection)
        self.layout.addWidget(self.btn_next)

        self.btn_quit = QPushButton("❌ Quit")
        self.btn_quit.clicked.connect(self.close)
        self.layout.addWidget(self.btn_quit)

        self.central_widget.setLayout(self.layout)

        # State variables
        self.user_mood = None
        self.music_player = QMediaPlayer()

    def handle_mood_selection(self):
        """Triggered when user clicks "Next" after choosing Happy or Stressed."""
        if self.radio_happy.isChecked():
            print("✅ User selected Happy")
            self.user_mood = "Happy"
            self.close()
            self.music_choice_window = MusicChoiceWindow()
            self.music_choice_window.show()
        elif self.radio_stressed.isChecked():
            print("✅ User selected Stressed")
            self.user_mood = "Stressed"
            self.close()
            self.mood_rating_window = stressed_support.MoodRatingWindow()
            print("✅ MoodRatingWindow initialized")
            self.mood_rating_window.show()
        else:
            QMessageBox.warning(self, "Warning", "Please select Happy or Stressed before proceeding.")

        print(f"User mood updated to: {self.user_mood}")
        # response = self.model.updateUser(email, password, first_name, last_name, dob, gender)


class MusicChoiceWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Music Choice")
        self.setGeometry(400, 200, 400, 300)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout()

        self.label_question = QLabel("You're happy today! Do you want me to play music?")
        self.layout.addWidget(self.label_question)

        # Play Music Button
        self.btn_yes = QPushButton("Yes 🎵")
        self.btn_yes.clicked.connect(self.play_random_song)
        self.layout.addWidget(self.btn_yes)

        # Stop Music Button (Initially Disabled)
        self.btn_stop = QPushButton("🛑 Stop Music")
        self.btn_stop.setEnabled(False)  # Disabled at first
        self.btn_stop.clicked.connect(self.stop_music)
        self.layout.addWidget(self.btn_stop)

        # Motivation Button
        self.btn_no = QPushButton("No, give me motivation 💪")
        self.btn_no.clicked.connect(self.show_motivation)
        self.layout.addWidget(self.btn_no)

        # Navigation Buttons
        self.btn_back = QPushButton("← Back")
        self.btn_back.clicked.connect(self.go_back)
        self.layout.addWidget(self.btn_back)

        self.btn_quit = QPushButton("❌ Quit")
        self.btn_quit.clicked.connect(self.close)
        self.layout.addWidget(self.btn_quit)

        self.central_widget.setLayout(self.layout)

        # Initialize Music Player
        self.music_player = QMediaPlayer()

    def play_random_song(self):
        """Randomly selects one song from the MUSIC_FOLDER and plays it."""
        try:
            songs = [f for f in os.listdir(MUSIC_FOLDER) if f.lower().endswith('.mp3')]
            if not songs:
                QMessageBox.information(self, "Info", "No songs found in the 'music' folder.")
                return

            random_song = random.choice(songs)
            full_path = os.path.abspath(os.path.join(MUSIC_FOLDER, random_song))
            url = QUrl.fromLocalFile(full_path)
            content = QMediaContent(url)

            # Stop any currently playing media
            if self.music_player.state() == QMediaPlayer.PlayingState:
                self.music_player.stop()

            self.music_player.setMedia(content)
            self.music_player.play()

            # Enable the Stop button when music starts playing
            self.btn_stop.setEnabled(True)

            QMessageBox.information(self, "Playing Music", f"Now playing: {random_song}")
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Error playing music: {e}")

    def stop_music(self):
        """Stops the currently playing song."""
        if self.music_player.state() == QMediaPlayer.PlayingState:
            self.music_player.stop()
            self.btn_stop.setEnabled(False)  # Disable Stop button when music is stopped
            QMessageBox.information(self, "Music Stopped", "Music has been stopped.")

    def show_motivation(self):
        """Switch to the motivation window."""
        self.close()
        self.motivation_window = MotivationWindow()
        self.motivation_window.show()

    def go_back(self):
        """Return to the main mood tracker."""
        self.close()
        self.mood_tracker = MoodTracker()
        self.mood_tracker.show()


class MotivationWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Motivational Message")
        self.setGeometry(400, 200, 400, 300)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout()

        self.label_message = QLabel(self.get_random_motivation(), self)
        self.layout.addWidget(self.label_message)

        # Navigation Buttons
        self.btn_back = QPushButton("← Back")
        self.btn_back.clicked.connect(self.go_back)
        self.layout.addWidget(self.btn_back)

        self.btn_quit = QPushButton("❌ Quit")
        self.btn_quit.clicked.connect(self.close)
        self.layout.addWidget(self.btn_quit)

        self.central_widget.setLayout(self.layout)

    def get_random_motivation(self):
        """Randomly selects a text file from the MESSAGES_FOLDER and returns its content."""
        try:
            msgs = [f for f in os.listdir(MESSAGES_FOLDER) if f.lower().endswith('.txt')]
            if not msgs:
                return "No motivational messages found."

            random_msg_file = random.choice(msgs)
            full_path = os.path.abspath(os.path.join(MESSAGES_FOLDER, random_msg_file))

            with open(full_path, 'r', encoding='utf-8') as f:
                return f.read().strip()

        except Exception as e:
            return f"Error reading message: {e}"

    def go_back(self):
        """Return to the main mood tracker."""
        self.close()
        self.mood_tracker = MoodTracker()
        self.mood_tracker.show()


def main():
    app = QApplication(sys.argv)
    window = MoodTracker()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()