from typing import Dict
from .philosophy import Philosophy, PhilosophyEffects
from .philosophy_enum import PhilosophyEnum
from .philosophy_effects import SpecialEffect

class PhilosophyAxis:
    def __init__(self, name: str, positive: Philosophy, negative: Philosophy):
        self.name = name
        # The 'positive'/'negative' labels here represent the two poles of the axis.
        self.pole1 = positive 
        self.pole2 = negative

# Define all philosophy axes with zero-sum effects
PHILOSOPHY_AXES: Dict[str, PhilosophyAxis] = {
    "SocietyFocus": PhilosophyAxis(
        "Society Focus",
        Philosophy(
            PhilosophyEnum.INDIVIDUALISM.value, 
            PhilosophyEffects(happiness=1, production=-1, money=1, resources=0, religion=0, environment=0, morale=-1, fertility=0)
        ),
        Philosophy(
            PhilosophyEnum.COLLECTIVISM.value, 
            PhilosophyEffects(happiness=-1, production=1, money=-1, resources=0, religion=0, environment=0, morale=1, fertility=0)
        )
    ),
    "WorldInteraction": PhilosophyAxis(
        "World Interaction",
        Philosophy(
            PhilosophyEnum.TECHNOCRACY.value, 
            PhilosophyEffects(happiness=0, production=2, money=1, resources=1, religion=-1, environment=-2, morale=0, fertility=-1)
        ),
        Philosophy(
            PhilosophyEnum.NATURALISM.value, 
            PhilosophyEffects(happiness=0, production=-2, money=-1, resources=-1, religion=1, environment=2, morale=0, fertility=1)
        )
    ),
    "GrowthStrategy": PhilosophyAxis(
        "Growth Strategy",
        Philosophy(
            PhilosophyEnum.EXPANSIONISM.value, 
            PhilosophyEffects(happiness=-1, production=1, money=1, resources=1, religion=-2, environment=-1, morale=1, fertility=0)
        ),
        Philosophy(
            PhilosophyEnum.CONSERVATION.value, 
            PhilosophyEffects(happiness=1, production=-1, money=-1, resources=-1, religion=2, environment=1, morale=-1, fertility=0)
        )
    ),
    "SocialStructure": PhilosophyAxis(
        "Social Structure",
        Philosophy(
            PhilosophyEnum.HIERARCHY.value, 
            PhilosophyEffects(happiness=-1, production=1, money=0, resources=0, religion=0, environment=0, morale=2, fertility=-2)
        ),
        Philosophy(
            PhilosophyEnum.FLUIDITY.value, 
            PhilosophyEffects(happiness=1, production=-1, money=0, resources=0, religion=0, environment=0, morale=-2, fertility=2)  
        )
    ),
    "InformationPolicy": PhilosophyAxis(
        "Information Policy",
        Philosophy(
            PhilosophyEnum.INFORMATION_FREEDOM.value, 
            PhilosophyEffects(happiness=1, production=1, money=0, resources=0, religion=-1, environment=0, morale=-1, fertility=0)
        ),
        Philosophy(
            PhilosophyEnum.KNOWLEDGE_CONTROL.value, 
            # Now strictly negating the positive effects:
            PhilosophyEffects(happiness=-1, production=-1, money=0, resources=0, religion=1, environment=0, morale=1, fertility=0)
        )
    ),
    "Ontology": PhilosophyAxis(
        "Ontology",
        Philosophy(
            PhilosophyEnum.MATERIALIST_RATIONALISM.value, 
            PhilosophyEffects(happiness=0, production=1, money=1, resources=0, religion=-1, environment=0, morale=0, fertility=-1)
        ),
        Philosophy(
            PhilosophyEnum.MYSTICISM.value, 
            PhilosophyEffects(happiness=1, production=-1, money=-1, resources=-1, religion=2, environment=0, morale=0, fertility=0)
        )
    ),
    "EthicsSystem": PhilosophyAxis(
        "Ethics System",
        Philosophy(
            PhilosophyEnum.DETERMINISTIC_ETHICS.value, 
            PhilosophyEffects(happiness=-1, production=0, money=-1, resources=0, religion=1, environment=0, morale=1, fertility=0)
        ),
        Philosophy(
            PhilosophyEnum.SITUATIONAL_ETHICS.value, 
            PhilosophyEffects(happiness=1, production=-1, money=0, resources=0, religion=-1, environment=0, morale=-1, fertility=2)
        )
    ),
    "ExistenceMode": PhilosophyAxis(
        "Existence Mode",
        Philosophy(
            PhilosophyEnum.VIRTUAL_EXODUS.value, 
            PhilosophyEffects(happiness=1, production=-1, money=1, resources=-1, religion=0, environment=1, morale=1, fertility=-2)
        ),
        Philosophy(
            PhilosophyEnum.PHYSICAL_BINDING.value, 
            PhilosophyEffects(happiness=-1, production=1, money=-1, resources=1, religion=0, environment=-1, morale=0, fertility=1)
        )
    ),
    "ResourceManagement": PhilosophyAxis(
        "Resource Management",
        Philosophy(
            PhilosophyEnum.DISTRIBUTIVE_AUTARKY.value, 
            PhilosophyEffects(happiness=0, production=-1, money=-1, resources=1, religion=0, environment=0, morale=1, fertility=0)
        ),
        Philosophy(
            PhilosophyEnum.CENTRALIZED_RESOURCES.value, 
            PhilosophyEffects(happiness=-1, production=1, money=1, resources=-1, religion=0, environment=0, morale=0, fertility=0)
        )
    ),
    "EmotionalExpression": PhilosophyAxis(
        "Emotional Expression",
        Philosophy(
            PhilosophyEnum.EMOTIONAL_CULTIVATION.value, 
            PhilosophyEffects(happiness=2, production=-1, money=0, resources=-1, religion=0, environment=0, morale=-1, fertility=1)
        ),
        Philosophy(
            PhilosophyEnum.AFFECTIVE_NEUTRALITY.value, 
            PhilosophyEffects(happiness=-2, production=1, money=0, resources=1, religion=0, environment=0, morale=1, fertility=-1)
        )
    ),
    "InterspeciesRelations": PhilosophyAxis(
        "Interspecies Relations",
        Philosophy(
            PhilosophyEnum.XENOBIOLOGICAL_INTEGRATION.value, 
            PhilosophyEffects(happiness=1, production=-1, money=-1, resources=-1, religion=0, environment=2, morale=0, fertility=0)
        ),
        Philosophy(
            PhilosophyEnum.SPECIES_SEPARATISM.value, 
            PhilosophyEffects(happiness=-1, production=0, money=0, resources=0, religion=1, environment=0, morale=1, fertility=-1)
        )
    ),
    "RealityPerception": PhilosophyAxis(
        "Reality Perception",
        Philosophy(
            PhilosophyEnum.CONSENSUS_REALITY.value, 
            PhilosophyEffects(happiness=-2, production=0, money=0, resources=0, religion=1, environment=0, morale=1, fertility=0)
        ),
        Philosophy(
            PhilosophyEnum.SUBJECTIVE_TRUTH.value, 
            PhilosophyEffects(happiness=2, production=0, money=0, resources=0, religion=-1, environment=0, morale=-1, fertility=0)
        )
    ),
    "BondingBasis": PhilosophyAxis(
        "Bonding Basis",
        Philosophy(
            PhilosophyEnum.CHOSEN_ASSOCIATION.value, 
            PhilosophyEffects(happiness=1, production=0, money=1, resources=0, religion=0, environment=0, morale=-1, fertility=-1)
        ),
        Philosophy(
            PhilosophyEnum.KINSHIP_BINDING.value, 
            PhilosophyEffects(happiness=-1, production=0, money=-1, resources=0, religion=0, environment=0, morale=1, fertility=1)
        )
    ),
    "InteractionStyle": PhilosophyAxis(
        "Interaction Style",
        Philosophy(
            PhilosophyEnum.SPONTANEOUS_AUTHENTICITY.value, 
            PhilosophyEffects(happiness=1, production=-1, money=0, resources=0, religion=0, environment=0, morale=-1, fertility=1)
        ),
        Philosophy(
            PhilosophyEnum.CODIFIED_INTERACTION.value, 
            PhilosophyEffects(happiness=-1, production=1, money=0, resources=0, religion=0, environment=0, morale=1, fertility=-1)
        )
    ),
    "WorldviewTimeline": PhilosophyAxis(
        "Worldview Timeline",
        Philosophy(
            PhilosophyEnum.LINEAR_PROGRESS.value, 
            PhilosophyEffects(happiness=0, production=1, money=1, resources=0, religion=-1, environment=-1, morale=0, fertility=0)
        ),
        Philosophy(
            PhilosophyEnum.CYCLIC_WORLDVIEW.value, 
            PhilosophyEffects(happiness=0, production=-1, money=-1, resources=0, religion=1, environment=1, morale=0, fertility=0)
        )
    ),
    "Excellence": PhilosophyAxis(
        "Excellence",
        Philosophy(
            PhilosophyEnum.EXCLUSIVE_EXCELLENCE.value, 
            PhilosophyEffects(happiness=-2, production=2, money=-1, resources=0, religion=0, environment=0, morale=1, fertility=0)
        ),
        Philosophy(
            PhilosophyEnum.INCLUSIVE_ACCESSIBILITY.value, 
            PhilosophyEffects(happiness=2, production=-2, money=0, resources=0, religion=0, environment=0, morale=0, fertility=0)
        )
    ),
    "Approach": PhilosophyAxis(
        "Approach",
        Philosophy(
            PhilosophyEnum.EXTREMISM.value, 
            PhilosophyEffects(
                happiness=-1, production=0, money=0, resources=0, 
                religion=1, environment=0, morale=0, fertility=0,
                special_effect=SpecialEffect.DOUBLE_ALL_EFFECTS
            )
        ),
        Philosophy(
            PhilosophyEnum.MIDDLE_WAY.value, 
            PhilosophyEffects(
                happiness=1, production=0, money=0, resources=0, 
                religion=-1, environment=0, morale=0, fertility=0
            )
        )
    ),
    "LifestyleMotivation": PhilosophyAxis(
        "Lifestyle Motivation",
        Philosophy(
            PhilosophyEnum.HEDONISM.value, 
            PhilosophyEffects(happiness=0, production=0, money=0, resources=3, religion=-1, environment=0, morale=-1, fertility=-1)
        ),
        Philosophy(
            PhilosophyEnum.MASOCHISM.value, 
            PhilosophyEffects(happiness=0, production=-1, money=0, resources=-1, religion=1, environment=0, morale=1, fertility=0)
        )
    ),
    "Governance": PhilosophyAxis(
        "Governance",
        Philosophy(
            PhilosophyEnum.BUREAUCRACY.value, 
            PhilosophyEffects(happiness=-1, production=1, money=-1, resources=0, religion=0, environment=0, morale=1, fertility=0)
        ),
        Philosophy(
            PhilosophyEnum.ANARCHIC_ADMINISTRATION.value, 
            PhilosophyEffects(happiness=0, production=0, money=1, resources=0, religion=0, environment=0, morale=-1, fertility=0)
        )
    ),
    "EconomicSystem": PhilosophyAxis(
        "Economic System",
        Philosophy(
            PhilosophyEnum.CAPITALISM.value, 
            PhilosophyEffects(happiness=-1, production=1, money=2, resources=-1, religion=0, environment=-1, morale=0, fertility=0)
        ),
        Philosophy(
            PhilosophyEnum.PLANNED_ECONOMY.value, 
            PhilosophyEffects(happiness=0, production=-1, money=-2, resources=2, religion=0, environment=0, morale=1, fertility=0)
        )
    ),
}
