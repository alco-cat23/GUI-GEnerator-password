
import sys
import random
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel


def generate_password(length=12):
    password_characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
    password = ''.join(random.choice(password_characters) for i in range(length))
    return password

class PasswordGeneratorApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Генератор пароля")
        self.setGeometry(400, 400, 640, 480)

        self.main_text = QLabel(self)
        self.main_text.setText("Типо пароль: " + generate_password(12))
        self.main_text.setGeometry(200,200,200,200)

        self.generate_button = QPushButton("Сгенерировать новый пароль", self)
        self.generate_button.clicked.connect(self.update_password)
        self.generate_button.setGeometry(200,250,200,40)

    def update_password(self):
        new_password = generate_password(12)
        self.main_text.setText("Типо пароль: " + new_password)


def application():
    app = QApplication(sys.argv)
    window = PasswordGeneratorApp()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    application()
