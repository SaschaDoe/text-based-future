from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton, QListWidget, QTableWidget, QTableWidgetItem, QHeaderView
from PySide6.QtCore import Qt
from ..Game.Civilisation_Generator.civilisation_generator import Civilization

class CivilizationGenerator(QWidget):
    def __init__(self):
        super().__init__()
        self.civilization = Civilization()
        layout = QVBoxLayout(self)
        layout.setAlignment(Qt.AlignCenter)
        layout.setSpacing(20)
        
        title = QLabel("Civilization Generator")
        title.setStyleSheet("""
            QLabel {
                color: #00ffff;
                font-size: 24px;
                font-weight: bold;
            }
        """)
        layout.addWidget(title)
        
        # Create list widget for philosophies
        self.philosophy_list = QListWidget()
        self.philosophy_list.setStyleSheet("""
            QListWidget {
                background-color: #1a1a3a;
                color: #00ffff;
                border: 2px solid #00ffff;
                border-radius: 5px;
                padding: 10px;
                font-size: 16px;
            }
            QListWidget::item {
                padding: 5px;
            }
        """)
        layout.addWidget(self.philosophy_list)
        
        # Create effects table
        self.effects_table = QTableWidget()
        self.effects_table.setColumnCount(8)
        self.effects_table.setRowCount(1)
        self.effects_table.setHorizontalHeaderLabels([
            "Happiness", "Production", "Money", "Resources",
            "Religion", "Pollution", "Morale", "Fertility"
        ])
        self.effects_table.setStyleSheet("""
            QTableWidget {
                background-color: #1a1a3a;
                color: #00ffff;
                border: 2px solid #00ffff;
                border-radius: 5px;
                padding: 10px;
                font-size: 14px;
            }
            QHeaderView::section {
                background-color: #2a2a4a;
                color: #00ffff;
                padding: 5px;
                border: 1px solid #00ffff;
            }
        """)
        header = self.effects_table.horizontalHeader()
        header.setSectionResizeMode(QHeaderView.Stretch)
        layout.addWidget(self.effects_table)
        
        # Create generate button
        generate_button = QPushButton("Generate Random Civilization")
        generate_button.clicked.connect(self.generate_civilization)
        layout.addWidget(generate_button)
        
    def generate_civilization(self):
        self.civilization.generate_random_philosophies()
        self.philosophy_list.clear()
        self.philosophy_list.addItems(self.civilization.get_philosophy_names())
        
        # Update effects table
        effects = self.civilization.get_total_effects()
        for i, (effect, value) in enumerate(effects.items()):
            item = QTableWidgetItem(str(value))
            item.setTextAlignment(Qt.AlignCenter)
            if value > 0:
                item.setForeground(Qt.green)
            elif value < 0:
                item.setForeground(Qt.red)
            self.effects_table.setItem(0, i, item) 