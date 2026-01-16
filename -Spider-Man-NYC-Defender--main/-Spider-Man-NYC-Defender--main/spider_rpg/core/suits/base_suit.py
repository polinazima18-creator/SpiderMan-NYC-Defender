from abc import ABC, abstractmethod
from dataclasses import dataclass


@dataclass
class SuitStats:
    name: str
    base_damage: int
    defense: int
    description: str


class SpiderSuit(ABC):
    def __init__(self, stats: SuitStats):
        self.stats = stats

    @abstractmethod
    def attack_modifier(self, base_damage: int) -> int:
        pass

    @abstractmethod
    def defend_modifier(self, incoming_damage: int) -> int:
        pass

    @abstractmethod
    def special_ability(self) -> str:
        pass

    def __str__(self):
        return self.stats.name
