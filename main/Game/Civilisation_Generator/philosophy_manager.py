from typing import Dict, List
import random
from .philosophy_set import PhilosophySet
from .philosophy_axes import PHILOSOPHY_AXES

class PhilosophyManager:
    def __init__(self):
        self.philosophy_set = PhilosophySet()
        
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
                
    def get_philosophy_names(self) -> List[str]:
        return [philosophy.value for philosophy in self.philosophy_set.philosophies.values()]
    
    def get_total_effects(self) -> Dict[str, float]:
        return self.philosophy_set.get_total_effects()
        
    def get_formatted_philosophies(self) -> List[str]:
        return [f"{axis}: {philosophy}" for axis, philosophy in self.philosophy_set.philosophies.items()] 