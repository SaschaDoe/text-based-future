from typing import Dict, List
from .philosophy import Philosophy
from .philosophy_effects import PhilosophyEffects, SpecialEffect
from .philosophy_enum import PhilosophyEnum
from .philosophy_axes import PHILOSOPHY_AXES

class PhilosophySet:
    def __init__(self):
        self.philosophies: Dict[str, PhilosophyEnum] = {}
        self.modifiers: Dict[str, float] = {}
        
    def add_philosophy(self, axis_name: str, philosophy: PhilosophyEnum):
        self.philosophies[axis_name] = philosophy
        self._update_modifiers()
        
    def remove_philosophy(self, axis_name: str):
        if axis_name in self.philosophies:
            del self.philosophies[axis_name]
            self._update_modifiers()
            
    def _update_modifiers(self):
        """Update effect modifiers based on current philosophy set"""
        self.modifiers = {}
        
        # Check for special effects in all philosophies
        for axis_name, philosophy_enum in self.philosophies.items():
            axis = PHILOSOPHY_AXES[axis_name]
            if axis.pole1.name == philosophy_enum:
                philosophy = axis.pole1
            else:
                philosophy = axis.pole2
                
            if philosophy.effects.special_effect == SpecialEffect.DOUBLE_ALL_EFFECTS:
                self.modifiers['all'] = 2.0  # Double all effects
                break  # We only need one extremism to double all effects
            
    def get_total_effects(self) -> Dict[str, float]:
        """Calculate total effects with modifiers applied"""
        total = PhilosophyEffects()
        
        # First, sum up all base effects
        for axis_name, philosophy_enum in self.philosophies.items():
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
        
        # Apply modifiers
        effects_dict = total.to_dict()
        if 'all' in self.modifiers:
            multiplier = self.modifiers['all']
            effects_dict = {k: v * multiplier for k, v in effects_dict.items()}
            
        return effects_dict 