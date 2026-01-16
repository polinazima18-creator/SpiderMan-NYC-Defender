from abc import ABC, abstractmethod


class CombatStrategy(ABC):
    """
    Інтерфейс для бойових стратегій.
    Кожна стратегія (удар, павутиння, гаджет) реалізує цей метод.
    """

    @abstractmethod
    def execute(self, attacker, defender) -> str:
        """
        Виконує дію атакуючого на захисника.
        Повертає рядок із описом результату для логу.
        """
        pass
