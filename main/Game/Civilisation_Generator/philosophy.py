from typing import Dict
from .philosophy_effects import PhilosophyEffects

class Philosophy:
    def __init__(self, name: str, effects: PhilosophyEffects):
        self.name = name
        self.effects = effects

    def get_effects_dict(self) -> Dict[str, int]:
        return self.effects.to_dict() 