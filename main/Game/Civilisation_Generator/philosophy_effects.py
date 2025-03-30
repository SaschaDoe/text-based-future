from dataclasses import dataclass
from typing import Dict

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