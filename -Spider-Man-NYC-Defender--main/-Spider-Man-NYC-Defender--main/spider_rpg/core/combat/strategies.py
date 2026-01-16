import random
from .base_strategy import CombatStrategy


class NormalAttack(CombatStrategy):
    """Звичайна атака рукопаш."""

    def execute(self, attacker, defender) -> str:
        raw_damage = attacker.attack()
        final_damage = defender.take_damage(raw_damage)
        return f"👊 {attacker.name} б'є {defender.name} і завдає {final_damage} шкоди!"


class WebShot(CombatStrategy):
    """Постріл павутинням."""

    def execute(self, attacker, defender) -> str:
        damage = 15
        actual = defender.take_damage(damage)
        return f"🕸️ {attacker.name} заліплює очі ворогу павутинням! ({actual} шкоди)"


class ImpactWeb(CombatStrategy):
    """Ударна павутина."""

    def execute(self, attacker, defender) -> str:
        dmg = int(attacker.base_attack * 1.5) + 5
        actual = defender.take_damage(dmg)
        return f"💥 {attacker.name} стріляє Ударною Павутиною! ({actual} шкоди)"


class FinisherMove(CombatStrategy):
    """Фінальний удар."""

    def execute(self, attacker, defender) -> str:
        if random.random() < 0.4:
            return f"💨 {attacker.name} намагається зробити сальто, але ПРОМАХУЄТЬСЯ!"
        raw_dmg = attacker.attack() * 3
        actual = defender.take_damage(raw_dmg)
        return f"⚡ НЕЙМОВІРНО! КРИТИЧНА ШКОДА ({actual})!"
