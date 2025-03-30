import random
from typing import Dict, List
from .philosophy import Philosophy
from .philosophy_effects import PhilosophyEffects
from .philosophy_axes import PHILOSOPHY_AXES
from .philosophy_enum import PhilosophyEnum
from .philosophy_set import PhilosophySet
from .background_generator import BackgroundGenerator, Background

class Civilization:
    def __init__(self):
        self.philosophy_set = PhilosophySet()
        self.backgrounds: List[Background] = []
        self._background_generator = BackgroundGenerator()
        
    def generate_random_philosophies(self):
        self.philosophy_set = PhilosophySet()
        
        # Determine number of philosophies based on probabilities
        rand = random.random() * 100
        if rand < 10:  # 10% chance for 1
            num_philosophies = 1
        elif rand < 70:  # 60% chance for 2
            num_philosophies = 2
        elif rand < 90:  # 20% chance for 3
            num_philosophies = 3
        else:  # 10% chance for 4
            num_philosophies = 4
            
        # Randomly select philosophy axes
        selected_axes = random.sample(list(PHILOSOPHY_AXES.items()), num_philosophies)
        
        # For each axis, randomly choose either positive or negative philosophy
        for axis_name, axis in selected_axes:
            if random.random() < 0.5:
                self.philosophy_set.add_philosophy(axis_name, axis.pole1.name)
            else:
                self.philosophy_set.add_philosophy(axis_name, axis.pole2.name)
                
    def generate_backgrounds(self):
        """Generate random backgrounds for the civilization"""
        self.backgrounds = self._background_generator.generate_backgrounds()
                
    def get_philosophy_names(self) -> List[str]:
        return [philosophy.value for philosophy in self.philosophy_set.philosophies.values()]
    
    def get_total_effects(self) -> Dict[str, float]:
        return self.philosophy_set.get_total_effects()
        
    def get_backgrounds(self) -> List[Background]:
        return self.backgrounds 