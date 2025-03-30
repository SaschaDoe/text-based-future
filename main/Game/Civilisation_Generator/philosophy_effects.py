from dataclasses import dataclass
from typing import Dict, List, Optional
from enum import Enum

class SpecialEffect(Enum):
    NONE = "none"
    DOUBLE_ALL_EFFECTS = "double_all_effects"
    # Add more special effects here as needed

@dataclass
class PhilosophyEffects:
    happiness: int = 0
    production: int = 0
    money: int = 0
    resources: int = 0
    religion: int = 0
    environment: int = 0
    morale: int = 0
    fertility: int = 0
    special_effect: SpecialEffect = SpecialEffect.NONE

    def __post_init__(self):
        self._validate_zero_sum()

    def _validate_zero_sum(self):
        total = sum([
            self.happiness,
            self.production,
            self.money,
            self.resources,
            self.religion,
            self.environment,
            self.morale,
            self.fertility
        ])
        if total != 0:
            raise ValueError(f"Philosophy effects must sum to zero, got {total}")

    def to_dict(self) -> Dict[str, int]:
        return {
            "Happiness": self.happiness,
            "Production": self.production,
            "Money": self.money,
            "Resources": self.resources,
            "Religion": self.religion,
            "Environment": self.environment,
            "Morale": self.morale,
            "Fertility": self.fertility
        } 