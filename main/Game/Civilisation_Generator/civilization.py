import random
from typing import Dict, List
import os
import requests
from .philosophy import Philosophy
from .philosophy_effects import PhilosophyEffects
from .philosophy_axes import PHILOSOPHY_AXES
from .philosophy_enum import PhilosophyEnum
from .philosophy_set import PhilosophySet
from .background_generator import BackgroundGenerator, Background
from .name_generator import NameGenerator, CivilizationProperties
from .philosophy_manager import PhilosophyManager
from .background_manager import BackgroundManager

class Civilization:
    def __init__(self, 
                 philosophy_manager: PhilosophyManager = None,
                 background_manager: BackgroundManager = None,
                 name_generator: NameGenerator = None):
        self.philosophy_manager = philosophy_manager or PhilosophyManager()
        self.background_manager = background_manager or BackgroundManager()
        self.name_generator = name_generator or NameGenerator()
        self.name = "Unnamed Civilization"
        
    def generate_name(self) -> str:
        try:
            properties = CivilizationProperties(
                philosophies=self.philosophy_manager.get_formatted_philosophies(),
                backgrounds=self.background_manager.get_formatted_backgrounds()
            )
            return self.name_generator.generate_name(properties)
        except Exception as e:
            return "Unknown Civilization"
        
    def generate_random_philosophies(self):
        self.philosophy_manager.generate_random_philosophies()
                
    def generate_backgrounds(self):
        self.background_manager.generate_backgrounds()
                
    def get_philosophy_names(self) -> List[str]:
        return self.philosophy_manager.get_philosophy_names()
    
    def get_total_effects(self) -> Dict[str, float]:
        return self.philosophy_manager.get_total_effects()
        
    def get_backgrounds(self) -> List[Background]:
        return self.background_manager.get_backgrounds() 