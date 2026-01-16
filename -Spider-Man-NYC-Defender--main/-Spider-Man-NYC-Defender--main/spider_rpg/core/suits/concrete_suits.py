from .base_suit import SpiderSuit, SuitStats


class ClassicSuit(SpiderSuit):
    """Класичний костюм. Збалансований."""

    def __init__(self):
        super().__init__(SuitStats(
            name="Classic Suit",
            base_damage=10,
            defense=5,
            description="Надійний класичний червоно-синій костюм."
        ))

    def attack_modifier(self, base_damage: int) -> int:
        return base_damage + self.stats.base_damage

    def defend_modifier(self, incoming_damage: int) -> int:
        damage = incoming_damage - self.stats.defense
        return max(0, damage)

    def special_ability(self) -> str:
        return "Web Shooter Barrage (Шквал павутиння)"


class SymbioteSuit(SpiderSuit):
    """Чорний костюм. Висока атака, ризик."""

    def __init__(self):
        super().__init__(SuitStats(
            name="Symbiote Suit",
            base_damage=25,
            defense=0,
            description="Живий іншопланетний організм. Підвищує агресію."
        ))

    def attack_modifier(self, base_damage: int) -> int:
        return int(base_damage * 1.5) + self.stats.base_damage

    def defend_modifier(self, incoming_damage: int) -> int:
        return incoming_damage

    def special_ability(self) -> str:
        return "Symbiote Tendrils (Щупальця симбіота)"


class IronSpiderSuit(SpiderSuit):
    """Залізний Павук. Високий захист."""

    def __init__(self):
        super().__init__(SuitStats(
            name="Iron Spider",
            base_damage=15,
            defense=15,
            description="Технологічний шедевр Тоні Старка."
        ))

    def attack_modifier(self, base_damage: int) -> int:
        return base_damage + self.stats.base_damage

    def defend_modifier(self, incoming_damage: int) -> int:
        reduced = incoming_damage * 0.5
        damage = int(reduced) - self.stats.defense
        return max(0, damage)

    def special_ability(self) -> str:
        return "Waldoes Stab (Удар маніпуляторами)"
