from typing import List
from .background_generator import BackgroundGenerator, Background

class BackgroundManager:
    def __init__(self, background_generator: BackgroundGenerator = None):
        self._background_generator = background_generator or BackgroundGenerator()
        self.backgrounds: List[Background] = []
        
    def generate_backgrounds(self):
        """Generate random backgrounds for the civilization"""
        self.backgrounds = self._background_generator.generate_backgrounds()
        
    def get_backgrounds(self) -> List[Background]:
        return self.backgrounds
        
    def get_formatted_backgrounds(self) -> List[str]:
        return [f"{bg.type.value}: {bg.name}" for bg in self.backgrounds] 