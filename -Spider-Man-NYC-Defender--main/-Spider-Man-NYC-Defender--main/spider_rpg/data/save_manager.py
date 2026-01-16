import json
import os
from core.player import Player
from core.suits.concrete_suits import ClassicSuit, SymbioteSuit, IronSpiderSuit

SAVE_FILE = "data/savegame.json"


class SaveManager:
    @staticmethod
    def save_game(player: Player):
        data = {
            "name": player.name,
            "hp": player.hp,
            "max_hp": player.max_hp,
            "xp": player.xp,
            "suit_name": player.current_suit.stats.name
        }
        try:
            os.makedirs("data", exist_ok=True)
            with open(SAVE_FILE, "w", encoding="utf-8") as f:
                json.dump(data, f, indent=4)
            print("✅ Збережено!")
        except Exception as e:
            print(f"Помилка: {e}")

    @staticmethod
    def load_game() -> Player:
        if not os.path.exists(SAVE_FILE):
            print("Немає файлу збереження.")
            return None
        try:
            with open(SAVE_FILE, "r", encoding="utf-8") as f:
                data = json.load(f)

            p = Player(data["name"])
            p.hp = data["hp"]
            p.max_hp = data["max_hp"]
            p.xp = data["xp"]

            s_name = data["suit_name"]
            if s_name == "Symbiote Suit":
                p.equip_suit(SymbioteSuit())
            elif s_name == "Iron Spider":
                p.equip_suit(IronSpiderSuit())
            else:
                p.equip_suit(ClassicSuit())

            print("✅ Завантажено!")
            return p
        except Exception:
            return None