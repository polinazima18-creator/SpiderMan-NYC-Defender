import sys
from rich.console import Console
from rich.panel import Panel
from core.game import Game

console = Console()

def main() -> None:
    try:
        # ПРИБРАЛИ СМАЙЛИК, щоб рамка була рівною
        console.print(Panel.fit(
            "[bold red]SPIDER-MAN: NYC DEFENDER[/bold red]\n[italic white]Console RPG Project[/italic white]",
            border_style="red",
            padding=(1, 4)
        ))
        console.input("[bold yellow]Натисніть Enter, щоб розпочати...[/bold yellow]")

        game = Game()
        game.start()

    except KeyboardInterrupt:
        console.print("\n[bold red]Гру завершено примусово.[/bold red]")
        sys.exit(0)

if __name__ == "__main__":
    main()