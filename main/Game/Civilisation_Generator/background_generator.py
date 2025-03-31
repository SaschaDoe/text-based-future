import random
import mmap
import csv
from typing import List, Dict, Set
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor
from dataclasses import dataclass
from enum import Enum
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class BackgroundType(Enum):
    CULTURE = "Culture"
    SOCIAL_CLASS = "Social Class"
    PROFESSION = "Profession"
    ELEMENT = "Element"

@dataclass
class Background:
    type: BackgroundType
    name: str

class BackgroundGenerator:
    def __init__(self):
        self.cultures: List[str] = []
        self.social_classes: List[str] = []
        self.professions: List[str] = []
        self.elements: List[str] = []
        self._load_backgrounds()
        
    def _read_file_with_mmap(self, file_path: Path) -> List[str]:
        """Read a file using memory mapping"""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                # Use CSV reader to properly handle CSV files
                reader = csv.reader(f)
                # Read all rows and flatten the list
                lines = [item for row in reader for item in row if item.strip()]
                # Clean the lines
                cleaned_lines = []
                for line in lines:
                    cleaned_line = line.strip('"\' \t\r\n')
                    if cleaned_line and len(cleaned_line) > 1:
                        cleaned_lines.append(cleaned_line)
                
                logger.info(f"Loaded {len(cleaned_lines)} items from {file_path.name}")
                return cleaned_lines
        except Exception as e:
            logger.error(f"Error reading file {file_path}: {str(e)}")
            return []
    
    def _load_backgrounds(self):
        """Load all background lists in parallel using ThreadPoolExecutor"""
        resources_dir = Path(__file__).parent.parent.parent.parent / 'resources'
        
        with ThreadPoolExecutor(max_workers=4) as executor:
            future_cultures = executor.submit(self._read_file_with_mmap, resources_dir / 'modern_cultures.csv')
            future_social_classes = executor.submit(self._read_file_with_mmap, resources_dir / 'social_classes.csv')
            future_professions = executor.submit(self._read_file_with_mmap, resources_dir / 'general_professions.csv')
            future_elements = executor.submit(self._read_file_with_mmap, resources_dir / 'elements_list.csv')
            
            self.cultures = future_cultures.result()
            self.social_classes = future_social_classes.result()
            self.professions = future_professions.result()
            self.elements = future_elements.result()
            
            # Log the number of items loaded for each type
            logger.info(f"Loaded {len(self.cultures)} cultures")
            logger.info(f"Loaded {len(self.social_classes)} social classes")
            logger.info(f"Loaded {len(self.professions)} professions")
            logger.info(f"Loaded {len(self.elements)} elements")
    
    def generate_backgrounds(self) -> List[Background]:
        """Generate 1-3 random backgrounds"""
        num_backgrounds = random.randint(1, 3)
        backgrounds: List[Background] = []
        used_types: Set[BackgroundType] = set()
        
        # Define available types and their corresponding lists
        type_to_list = {
            BackgroundType.CULTURE: self.cultures,
            BackgroundType.SOCIAL_CLASS: self.social_classes,
            BackgroundType.PROFESSION: self.professions,
            BackgroundType.ELEMENT: self.elements
        }
        
        # Generate backgrounds
        while len(backgrounds) < num_backgrounds:
            # Choose a random type that hasn't been used yet
            available_types = [t for t in BackgroundType if t not in used_types and type_to_list[t]]
            if not available_types:
                break
                
            background_type = random.choice(available_types)
            name = random.choice(type_to_list[background_type])
            
            backgrounds.append(Background(background_type, name))
            used_types.add(background_type)
            
        return backgrounds 