from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton
from PySide6.QtCore import Qt

class GameSettings(QWidget):
    def __init__(self, on_next_clicked):
        super().__init__()
        self.on_next_clicked = on_next_clicked
        layout = QVBoxLayout(self)
        layout.setAlignment(Qt.AlignCenter)
        layout.setSpacing(20)
        
        title = QLabel("Game Settings")
        title.setStyleSheet("""
            QLabel {
                color: #00ffff;
                font-size: 24px;
                font-weight: bold;
            }
        """)
        layout.addWidget(title)
        
        next_button = QPushButton("NEXT")
        next_button.clicked.connect(on_next_clicked)
        layout.addWidget(next_button) 