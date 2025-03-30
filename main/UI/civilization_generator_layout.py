from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton, QListWidget, QTableWidget, QTableWidgetItem, QHeaderView, QListWidgetItem
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
        philosophy_label = QLabel("Philosophies:")
        philosophy_label.setStyleSheet("color: #00ffff; font-size: 16px;")
        layout.addWidget(philosophy_label)
        
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
        
        # Create list widget for backgrounds
        background_label = QLabel("Backgrounds:")
        background_label.setStyleSheet("color: #00ffff; font-size: 16px;")
        layout.addWidget(background_label)
        
        self.background_list = QListWidget()
        self.background_list.setStyleSheet("""
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
        layout.addWidget(self.background_list)
        
        # Create effects table
        self.effects_table = QTableWidget()
        self.effects_table.setColumnCount(8)
        self.effects_table.setRowCount(1)
        self.effects_table.setHorizontalHeaderLabels([
            "Happiness", "Production", "Money", "Resources",
            "Religion", "Environment", "Morale", "Fertility"
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
        
    def _create_effect_tooltip(self, philosophy):
        effects = philosophy.effects
        non_zero_effects = {
            "Happiness": effects.happiness,
            "Production": effects.production,
            "Money": effects.money,
            "Resources": effects.resources,
            "Religion": effects.religion,
            "Environment": effects.environment,
            "Morale": effects.morale,
            "Fertility": effects.fertility
        }
        non_zero_effects = {k: v for k, v in non_zero_effects.items() if v != 0}
        if not non_zero_effects:
            return ""
            
        tooltip = "<p style='margin: 0;'>Effects:</p>"
        for effect, value in non_zero_effects.items():
            sign = "+" if value > 0 else ""
            color = "#00ff00" if value > 0 else "#ff0000"
            tooltip += f"<p style='margin: 0; color: {color}'>{sign}{value} {effect}</p>"
        return tooltip
        
    def generate_civilization(self):
        self.civilization = Civilization()
        self.civilization.generate_random_philosophies()
        self.civilization.generate_backgrounds()
        
        # Clear existing items
        self.philosophy_list.clear()
        self.background_list.clear()
        
        # Add philosophy items
        for axis_name, philosophy_name in self.civilization.philosophy_set.philosophies.items():
            item = QListWidgetItem(f"{axis_name}: {philosophy_name}")
            self.philosophy_list.addItem(item)
            
        # Add background items
        for background in self.civilization.get_backgrounds():
            item = QListWidgetItem(f"{background.type.value}: {background.name}")
            self.background_list.addItem(item)
            
        # Update effects
        self.update_effects()
        
    def update_effects(self):
        effects = self.civilization.get_total_effects()
        for i, (effect, value) in enumerate(effects.items()):
            item = QTableWidgetItem(str(value))
            item.setTextAlignment(Qt.AlignCenter)
            if value > 0:
                item.setForeground(Qt.green)
            elif value < 0:
                item.setForeground(Qt.red)
            self.effects_table.setItem(0, i, item) 