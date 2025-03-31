import json
import requests
from pathlib import Path
from typing import List
from dataclasses import dataclass
from PySide6.QtWidgets import QMessageBox
from .groq_api import GroqApiCaller

@dataclass
class CivilizationProperties:
    philosophies: List[str]
    backgrounds: List[str]

class NameGenerator:
    def __init__(self):
        self.api_caller = GroqApiCaller()
    
    def generate_name(self, properties: CivilizationProperties) -> str:
        """Generate a civilization name using the Groq API"""
        try:
            prompt = self._create_prompt(properties)
            messages = [{
                "role": "user",
                "content": prompt
            }]
            
            return self.api_caller.call_api(messages)
                
        except Exception as e:
            return "Unknown Civilization"
    
    def _create_prompt(self, properties: CivilizationProperties) -> str:
        """Create a prompt for the AI based on civilization properties"""
        philosophies_str = ", ".join(properties.philosophies)
        backgrounds_str = ", ".join(properties.backgrounds)
        
        return f"""Generate a unique and fitting name for a civilization with the following characteristics:

Philosophies: {philosophies_str}
Backgrounds: {backgrounds_str}

The name should:
1. Be 2-4 words long
2. Reflect the civilization's philosophies and backgrounds
3. Sound like a proper civilization name
4. Be unique and memorable
5. Not include any offensive or inappropriate terms

Please provide only the name, without any additional text or explanation.""" 