import random
from typing import Dict, List
from .philosophy import Philosophy
from .philosophy_effects import PhilosophyEffects
from .philosophy_axes import PHILOSOPHY_AXES
from .philosophy_enum import PhilosophyEnum

class Civilization:
    def __init__(self):
        self.philosophies: Dict[str, PhilosophyEnum] = {}
        
    def generate_random_philosophies(self):
        self.philosophies.clear()
        
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
                self.philosophies[axis_name] = axis.pole1.name
            else:
                self.philosophies[axis_name] = axis.pole2.name
                
    def get_philosophy_names(self) -> List[str]:
        return [philosophy.value for philosophy in self.philosophies.values()]
    
    def get_total_effects(self) -> Dict[str, int]:
        total = PhilosophyEffects()
        
        for axis_name, philosophy_enum in self.philosophies.items():
            # Find the philosophy in the axis
            axis = PHILOSOPHY_AXES[axis_name]
            if axis.pole1.name == philosophy_enum:
                philosophy = axis.pole1
            else:
                philosophy = axis.pole2
                
            total.happiness += philosophy.effects.happiness
            total.production += philosophy.effects.production
            total.money += philosophy.effects.money
            total.resources += philosophy.effects.resources
            total.religion += philosophy.effects.religion
            total.environment += philosophy.effects.environment
            total.morale += philosophy.effects.morale
            total.fertility += philosophy.effects.fertility
                
        return total.to_dict() 