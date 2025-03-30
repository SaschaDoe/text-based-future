from PySide6.QtWidgets import QWidget, QVBoxLayout, QPushButton, QLabel
from PySide6.QtCore import Qt

class MainMenu(QWidget):
    def __init__(self, on_play_clicked, on_exit_clicked):
        super().__init__()
        self.on_play_clicked = on_play_clicked
        self.on_exit_clicked = on_exit_clicked
        layout = QVBoxLayout(self)
        layout.setAlignment(Qt.AlignCenter)
        layout.setSpacing(20)
        
        title = QLabel("ALPHA CENTAURI")
        title.setAlignment(Qt.AlignCenter)
        title.setStyleSheet("""
            QLabel {
                color: #00ffff;
                font-size: 24px;
                font-weight: bold;
            }
        """)
        layout.addWidget(title)
        
        play_button = QPushButton("PLAY")
        play_button.clicked.connect(on_play_clicked)
        layout.addWidget(play_button)
        
        exit_button = QPushButton("EXIT")
        exit_button.clicked.connect(on_exit_clicked)
        layout.addWidget(exit_button) 