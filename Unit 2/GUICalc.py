import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit, QPushButton, QGridLayout, QVBoxLayout
from PyQt5.QtCore import Qt

class mainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Calculator")
        self.setFixedSize(300, 400)
        main_layout = QVBoxLayout()
        self.display = QLineEdit()
        self.display.setReadOnly(True)
        self.display.setAlignment(Qt.AlignRight)
        self.display.setFixedHeight(50)
        main_layout.addWidget(self.display)

        button_layout = QGridLayout()
        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', '=', '+'
        ]

        row = 0
        col = 0
        for text in buttons:
            button = QPushButton(text)
            button.setFixedSize(60, 60)
            button.clicked.connect(self.on_button_clicked)
            button_layout.addWidget(button, row, col)
            col += 1
            if col > 3:
                col = 0
                row += 1

        clear_button = QPushButton("Clear")
        clear_button.setFixedSize(60, 60)
        clear_button.clicked.connect(self.clear_display)
        button_layout.addWidget(clear_button, row, 0)

        delete_button = QPushButton("Del")
        delete_button.setFixedSize(60, 60)
        delete_button.clicked.connect(self.delete_last_char)
        button_layout.addWidget(delete_button, row, 1, 1, 2)

        main_layout.addLayout(button_layout)
        self.setLayout(main_layout)

    def on_button_clicked(self):
        button = self.sender()
        text = button.text()

        if text == "=":
            try:
                result = str(eval(self.display.text()))
                self.display.setText(result)
            except Exception:
                self.display.setText("Error")
        else:
            current_text = self.display.text()
            if current_text == "Error":
                current_text = ""
            self.display.setText(current_text + text)

    def clear_display(self):
        self.display.clear()

    def delete_last_char(self):
        current_text = self.display.text()
        self.display.setText(current_text[:-1])


app = QApplication(sys.argv)
Calculator = mainWindow()
Calculator.show()
sys.exit(app.exec_())