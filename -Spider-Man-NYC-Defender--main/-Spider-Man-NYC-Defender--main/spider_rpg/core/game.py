import random
import time
from threading import Lock
from rich.console import Console
from rich.panel import Panel
from rich.table import Table

from core.player import Player
from core.suits.concrete_suits import ClassicSuit, SymbioteSuit, IronSpiderSuit
from core.enemies.factory import EnemyFactory
from core.combat.strategies import NormalAttack, WebShot, ImpactWeb, FinisherMove
from data.save_manager import SaveManager

console = Console()


class GameMeta(type):
    _instances = {}
    _lock = Lock()

    def __call__(cls, *args, **kwargs):
        with cls._lock:
            if cls not in cls._instances:
                cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]


class Game(metaclass=GameMeta):
    def __init__(self):
        self.is_running = False
        self.player = None
        self.current_enemy = None

    def start(self):
        self.is_running = True
        self.player = Player("Spider-Man")
        self._game_loop()

    def stop(self):
        self.is_running = False

    def _game_loop(self):
        console.clear()
        console.print(Panel("[bold red]SPIDER-MAN: NYC DEFENDER[/bold red]"))
        self._print_help()

        while self.is_running:
            cmd = console.input("\n[bold cyan][NYC] >> [/bold cyan]").strip().lower()

            if cmd == 'q':
                self.stop()
            elif cmd == 'help':
                self._print_help()
            elif cmd == 'save':
                SaveManager.save_game(self.player)
            elif cmd == 'load':
                p = SaveManager.load_game()
                if p: self.player = p
            elif cmd == 'patrol':
                self._patrol_event()
            elif cmd in ['attack', 'web', 'impact', 'finisher']:
                self._handle_combat(cmd)
            elif 'suit' in cmd:
                if 'classic' in cmd:
                    self.player.equip_suit(ClassicSuit())
                    console.print("[bold blue]>> Ви перевдягнулися у Classic Suit![/bold blue]")
                elif 'venom' in cmd:
                    self.player.equip_suit(SymbioteSuit())
                    console.print("[bold purple]>> Ви перевдягнулися у Symbiote Suit![/bold purple]")
                elif 'iron' in cmd:
                    self.player.equip_suit(IronSpiderSuit())
                    console.print("[bold red]>> Ви перевдягнулися у Iron Spider![/bold red]")
                else:
                    # Ось тут правильний рядок з кольорами:
                    console.print(
                        "Костюми: [bold blue]classic[/bold blue], [bold purple]venom[/bold purple], [bold red]iron[/bold red]")
            else:
                console.print("[red]Невідома команда[/red]")

    def _patrol_event(self):
        if self.current_enemy:
            console.print("[red]Спочатку переможіть ворога![/red]")
            return

        console.print("[dim]Патрулювання...[/dim]")
        time.sleep(0.5)
        roll = random.random()

        if roll < 0.3:
            self.player.hp = min(self.player.max_hp, self.player.hp + 10)
            console.print("[green]Все спокійно. Відновлено HP.[/green]")
        elif roll < 0.6:
            self.current_enemy = EnemyFactory.create_enemy("thug")
            console.print(f"[yellow]Ворог: {self.current_enemy.name}![/yellow]")
        elif roll < 0.85:
            self.current_enemy = EnemyFactory.create_enemy("goblin")
            console.print(f"[orange1]Ворог: {self.current_enemy.name}![/orange1]")
        else:
            self.current_enemy = EnemyFactory.create_enemy("venom")
            console.print(f"[bold purple]Ворог: {self.current_enemy.name}![/bold purple]")
        self._print_status()

    def _handle_combat(self, cmd):
        if not self.current_enemy:
            console.print("[yellow]Немає з ким битися.[/yellow]")
            return

        strategy = NormalAttack()
        if cmd == 'web':
            strategy = WebShot()
        elif cmd == 'impact':
            strategy = ImpactWeb()
        elif cmd == 'finisher':
            strategy = FinisherMove()

        console.print(f"[cyan]{strategy.execute(self.player, self.current_enemy)}[/cyan]")

        if not self.current_enemy.is_alive():
            console.print(f"[bold green]Перемога! +{self.current_enemy.xp_reward} XP[/bold green]")
            self.player.xp += self.current_enemy.xp_reward
            self.current_enemy = None
            return

        dmg, desc = self.current_enemy.attack_behavior()
        taken = self.player.take_damage(dmg)
        console.print(f"[red]{self.current_enemy.name}: {desc} (-{taken} HP)[/red]")
        self._print_status()

        if self.player.hp <= 0:
            console.print("[bold red]GAME OVER[/bold red]")
            self.stop()

    def _print_status(self):
        table = Table(title="Статус")
        table.add_column("Герой")
        table.add_column("HP")
        table.add_column("Костюм")
        if self.current_enemy:
            table.add_column("Ворог")
            table.add_column("HP Ворога")

        row = [self.player.name, str(self.player.hp), self.player.current_suit.stats.name]
        if self.current_enemy:
            row.extend([self.current_enemy.name, str(self.current_enemy.hp)])
        table.add_row(*row)
        console.print(table)

    def _print_help(self):
        """Виводить красиву таблицю команд."""
        table = Table(title="МЕНЮ ДІЙ", show_header=True, header_style="bold magenta")
        table.add_column("Команда", style="bold cyan", width=20)
        table.add_column("Опис", style="white")

        table.add_row("patrol", "Патрулювати місто (Знайти ворога)")
        table.add_row("attack", "Звичайна атака (Рукопаш)")
        table.add_row("web", "Постріл павутинням (Слабкий, точний)")
        table.add_row("impact", "Ударна павутина (Сильна)")
        table.add_row("finisher", "Ультра-удар (Ризик промаху!)")
        table.add_row("suit [name]", "Змінити костюм (classic, venom, iron)")
        table.add_row("save / load", "Зберегти / Завантажити гру")
        table.add_row("q", "Вихід з гри")

        console.print(table)