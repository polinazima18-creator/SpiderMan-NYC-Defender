from abc import ABC, abstractmethod


class BaseEnemy(ABC):
    def __init__(self, name: str, hp: int, damage: int, xp_reward: int):
        self.name = name
        self.hp = hp
        self.max_hp = hp
        self.damage = damage
        self.xp_reward = xp_reward

    def take_damage(self, amount: int) -> int:
        self.hp -= amount
        if self.hp < 0: self.hp = 0
        return amount

    def is_alive(self) -> bool:
        return self.hp > 0

    @abstractmethod
    def attack_behavior(self) -> tuple[int, str]:
        """
        Повертає кортеж: (кількість шкоди, текстовий опис атаки)
        Це дозволяє кожному ворогу мати свою логіку.
        """
        pass

    def __str__(self):
        return f"{self.name} (HP: {self.hp}/{self.max_hp})"
