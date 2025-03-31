import pytest
from unittest.mock import Mock
import sys
from pathlib import Path

# Add the project root to Python path
project_root = Path(__file__).parent.parent
sys.path.append(str(project_root))

from main.Game.Civilisation_Generator.civilization import Civilization
from main.Game.Civilisation_Generator.philosophy_manager import PhilosophyManager
from main.Game.Civilisation_Generator.background_manager import BackgroundManager
from main.Game.Civilisation_Generator.name_generator import NameGenerator
from main.Game.Civilisation_Generator.background_generator import Background, BackgroundType

@pytest.fixture
def mock_philosophy_manager():
    manager = Mock(spec=PhilosophyManager)
    manager.get_formatted_philosophies.return_value = ["SocietyFocus: Individualism"]
    manager.get_philosophy_names.return_value = ["Individualism"]
    manager.get_total_effects.return_value = {"Happiness": 1, "Production": -1}
    return manager

@pytest.fixture
def mock_background_manager():
    manager = Mock(spec=BackgroundManager)
    manager.get_formatted_backgrounds.return_value = ["Culture: Western"]
    manager.get_backgrounds.return_value = [
        Background(BackgroundType.CULTURE, "Western")
    ]
    return manager

@pytest.fixture
def mock_name_generator():
    generator = Mock(spec=NameGenerator)
    generator.generate_name.return_value = "Test Civilization"
    return generator

@pytest.fixture
def civilization(mock_philosophy_manager, mock_background_manager, mock_name_generator):
    return Civilization(
        philosophy_manager=mock_philosophy_manager,
        background_manager=mock_background_manager,
        name_generator=mock_name_generator
    )

def test_civilization_initialization(civilization):
    assert civilization.name == "Unnamed Civilization"
    assert isinstance(civilization.philosophy_manager, Mock)
    assert isinstance(civilization.background_manager, Mock)
    assert isinstance(civilization.name_generator, Mock)

def test_generate_name_success(civilization):
    name = civilization.generate_name()
    assert name == "Test Civilization"
    civilization.name_generator.generate_name.assert_called_once()

def test_generate_name_failure(civilization):
    civilization.name_generator.generate_name.side_effect = Exception("API Error")
    name = civilization.generate_name()
    assert name == "Unknown Civilization"

def test_generate_random_philosophies(civilization):
    civilization.generate_random_philosophies()
    civilization.philosophy_manager.generate_random_philosophies.assert_called_once()

def test_generate_backgrounds(civilization):
    civilization.generate_backgrounds()
    civilization.background_manager.generate_backgrounds.assert_called_once()

def test_get_philosophy_names(civilization):
    names = civilization.get_philosophy_names()
    assert names == ["Individualism"]
    civilization.philosophy_manager.get_philosophy_names.assert_called_once()

def test_get_total_effects(civilization):
    effects = civilization.get_total_effects()
    assert effects == {"Happiness": 1, "Production": -1}
    civilization.philosophy_manager.get_total_effects.assert_called_once()

def test_get_backgrounds(civilization):
    backgrounds = civilization.get_backgrounds()
    assert len(backgrounds) == 1
    assert backgrounds[0].type == BackgroundType.CULTURE
    assert backgrounds[0].name == "Western"
    civilization.background_manager.get_backgrounds.assert_called_once()

def test_default_initialization():
    civilization = Civilization()
    assert isinstance(civilization.philosophy_manager, PhilosophyManager)
    assert isinstance(civilization.background_manager, BackgroundManager)
    assert isinstance(civilization.name_generator, NameGenerator) 