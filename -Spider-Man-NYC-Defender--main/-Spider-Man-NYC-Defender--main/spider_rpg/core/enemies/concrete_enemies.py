import random
from .base_enemy import BaseEnemy


class Thug(BaseEnemy):
    def __init__(self):
        super().__init__("Вуличний Бандит", hp=30, damage=5, xp_reward=10)

    def attack_behavior(self) -> tuple[int, str]:
        if random.random() < 0.3:
            return self.damage * 2, "Бандит дістає пістолет і стріляє!"
        return self.damage, "Бандит розмахує ножем."


class GreenGoblin(BaseEnemy):
    def __init__(self):
        super().__init__("Зелений Гоблін", hp=80, damage=12, xp_reward=50)

    def attack_behavior(self) -> tuple[int, str]:

        roll = random.random()
        if roll < 0.4:
            return self.damage + 10, "🎃 Гоблін кидає Гарбузову Бомбу! Вибух!"
        elif roll < 0.7:
            return self.damage, "Гоблін таранить вас своїм глайдером!"
        else:
            return 0, "Гоблін сміється і промахується, літаючи колами!"


class Venom(BaseEnemy):
    def __init__(self):
        super().__init__("Веном", hp=150, damage=20, xp_reward=100)

    def attack_behavior(self) -> tuple[int, str]:
        if random.random() < 0.2 and self.hp < self.max_hp:
            heal = 20
            self.hp += heal
            return 0, f"🖤 Веном поглинає біомасу і лікується на {heal} HP!"
        return self.damage, "Веном атакує чорними щупальцями!"
