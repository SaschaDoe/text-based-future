from PySide6.QtWidgets import QMainWindow, QMenuBar, QMenu
from PySide6.QtCore import Qt
from .main_menu import MainMenu
from .game_settings_layout import GameSettings
from .civilization_generator_layout import CivilizationGenerator

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Alpha Centauri")
        self.setMinimumSize(800, 600)
        
        # Set dark theme
        self.setStyleSheet("""
            QMainWindow {
                background-color: #0a0a1a;
            }
            QPushButton {
                background-color: #1a1a3a;
                color: #00ffff;
                border: 2px solid #00ffff;
                border-radius: 5px;
                padding: 10px;
                font-size: 16px;
                min-width: 200px;
            }
            QPushButton:hover {
                background-color: #2a2a4a;
            }
            QLabel {
                color: #00ffff;
                font-size: 24px;
                font-weight: bold;
            }
            QMenuBar {
                background-color: #1a1a3a;
                color: #00ffff;
            }
            QMenuBar::item:selected {
                background-color: #2a2a4a;
            }
        """)
        
        # Create menu bar (hidden initially)
        self.menu_bar = self.menuBar()
        self.menu_bar.hide()
        self.create_menu_bar()
        
        # Start with main menu
        self.show_main_menu()
        
    def create_menu_bar(self):
        game_menu = self.menu_bar.addMenu("Game")
        exit_action = game_menu.addAction("Exit")
        exit_action.triggered.connect(self.close)
        
    def show_main_menu(self):
        self.menu_bar.hide()
        self.main_menu = MainMenu(self.start_game, self.close)
        self.setCentralWidget(self.main_menu)
        
    def start_game(self):
        self.menu_bar.show()
        self.game_settings = GameSettings(self.show_civilization_generator)
        self.setCentralWidget(self.game_settings)
        
    def show_civilization_generator(self):
        self.civilization_generator = CivilizationGenerator()
        self.setCentralWidget(self.civilization_generator) 