import random

class Philosophy:
    def __init__(self, name):
        self.name = name
        self.effects = self._get_effects()
    
    def _get_effects(self):
        effects = {
            "Pacifism": {"Happiness": 2, "Production": -1, "Money": 1, "Resources": 0, "Religion": 1, "Pollution": -1, "Morale": 1, "Fertility": 0},
            "Militarism": {"Happiness": -1, "Production": 2, "Money": -1, "Resources": -1, "Religion": 0, "Pollution": 1, "Morale": 2, "Fertility": 0},
            "Democracy": {"Happiness": 2, "Production": 0, "Money": 1, "Resources": 0, "Religion": -1, "Pollution": 0, "Morale": 1, "Fertility": 0},
            "Autocracy": {"Happiness": -1, "Production": 1, "Money": 0, "Resources": 1, "Religion": 0, "Pollution": 0, "Morale": -1, "Fertility": 0},
            "Environmentalist": {"Happiness": 1, "Production": -1, "Money": -1, "Resources": 1, "Religion": 0, "Pollution": -2, "Morale": 1, "Fertility": 1},
            "Industrialist": {"Happiness": -1, "Production": 2, "Money": 1, "Resources": -1, "Religion": 0, "Pollution": 2, "Morale": 0, "Fertility": -1},
            "Spiritualist": {"Happiness": 1, "Production": 0, "Money": -1, "Resources": 0, "Religion": 2, "Pollution": 0, "Morale": 1, "Fertility": 0},
            "Materialist": {"Happiness": -1, "Production": 1, "Money": 1, "Resources": 0, "Religion": -1, "Pollution": 1, "Morale": 0, "Fertility": 0},
            "Collectivist": {"Happiness": 0, "Production": 1, "Money": 0, "Resources": 1, "Religion": 0, "Pollution": 0, "Morale": 1, "Fertility": 0},
            "Individualist": {"Happiness": 1, "Production": 0, "Money": 1, "Resources": -1, "Religion": 0, "Pollution": 0, "Morale": -1, "Fertility": 0},
            "Diplomatic": {"Happiness": 1, "Production": 0, "Money": 1, "Resources": 0, "Religion": 0, "Pollution": 0, "Morale": 1, "Fertility": 0},
            "Isolationist": {"Happiness": -1, "Production": 0, "Money": -1, "Resources": 1, "Religion": 0, "Pollution": 0, "Morale": 0, "Fertility": 0}
        }
        return effects[self.name]

class Civilization:
    def __init__(self):
        self.philosophies = []
        
    def generate_random_philosophies(self):
        # Clear existing philosophies
        self.philosophies = []
        
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
            
        # List of possible philosophies
        available_philosophies = [
            "Pacifism", "Militarism", "Democracy", "Autocracy",
            "Environmentalist", "Industrialist", "Spiritualist", "Materialist",
            "Collectivist", "Individualist", "Diplomatic", "Isolationist"
        ]
        
        # Randomly select philosophies
        selected_philosophies = random.sample(available_philosophies, num_philosophies)
        self.philosophies = [Philosophy(name) for name in selected_philosophies]
        
    def get_philosophy_names(self):
        return [p.name for p in self.philosophies]
    
    def get_total_effects(self):
        total_effects = {
            "Happiness": 0, "Production": 0, "Money": 0, "Resources": 0,
            "Religion": 0, "Pollution": 0, "Morale": 0, "Fertility": 0
        }
        
        for philosophy in self.philosophies:
            for effect, value in philosophy.effects.items():
                total_effects[effect] += value
                
        return total_effects
