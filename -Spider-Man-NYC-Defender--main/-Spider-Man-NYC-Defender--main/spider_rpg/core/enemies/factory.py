from typing import Optional
from .base_enemy import BaseEnemy
from .concrete_enemies import Thug, GreenGoblin, Venom


class EnemyFactory:
    """
    Паттерн Factory Method.
    Централізоване створення об'єктів ворогів.
    """

    @staticmethod
    def create_enemy(enemy_type: str) -> Optional[BaseEnemy]:
        key = enemy_type.lower().strip()

        if key == "thug":
            return Thug()
        elif key == "goblin":
            return GreenGoblin()
        elif key == "venom":
            return Venom()
        else:
            print(f"Помилка: Невідомий тип ворога '{enemy_type}'")
            return None
