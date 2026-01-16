from core.suits.base_suit import SpiderSuit
from core.suits.concrete_suits import ClassicSuit


class Player:
    def __init__(self, name: str) -> None:
        self.name = name
        self.hp: int = 100
        self.max_hp: int = 100
        self.base_attack: int = 10
        self.xp: int = 0

        self.current_suit: SpiderSuit = ClassicSuit()

    def equip_suit(self, suit: SpiderSuit) -> None:
        """Смена костюма (Переключение состояния)."""
        self.current_suit = suit
        print(f"DEBUG: {self.name} надел {suit.stats.name}")

    def attack(self) -> int:
        """Делегируем расчет урона костюму."""
        return self.current_suit.attack_modifier(self.base_attack)

    def take_damage(self, amount: int) -> int:
        """Делегируем расчет защиты костюму."""
        actual_damage = self.current_suit.defend_modifier(amount)
        self.hp -= actual_damage
        if self.hp < 0:
            self.hp = 0
        return actual_damage

    def __str__(self) -> str:
        return (f"[{self.name}] HP: {self.hp}/{self.max_hp} | "
                f"Suit: {self.current_suit.stats.name}")
