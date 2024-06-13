from rich.console import Console
from rich.live import Live
from rich.panel import Panel

from coordinator import Coordinator

console = Console()


class Entity:
    prefix = ""

    def send_message(self, message: str) -> None:
        assert self.prefix
        console.print(f"{self.prefix} {message}")


class System(Entity):
    prefix = ":gear: [bold green]System:[/bold green]"


class AI(Entity):
    prefix = ":robot: [bold magenta]AI:[/bold magenta]"

    def __init__(self) -> None:
        self.coordinator = Coordinator()

    def query(self, message: str) -> None:
        with Live(console=console) as live:
            response = self.coordinator.invoke(message)
            live.update(self.__create_completed_panel(response))

    def __create_completed_panel(self, message: str):
        completed_message = (
            f"Status: [green]Completed![/green] \n {self.prefix} {message}"
        )
        panel = Panel(
            completed_message,
            title="AI Generating Response",
            title_align="left",
            border_style="magenta",
        )
        return panel


class TerminalDemo:
    def __init__(self) -> None:
        self.ai = AI()
        self.system = System()

    def run(self) -> None:
        self.system.send_message("Medical Multi Agent initialized")
        self.system.send_message("Type '/bye' to exit the program")
        while True:
            self.system.send_message("Enter your questions or commands:")
            message = input(
                ">>> ",
            ).strip()  # Using plain input to get user input
            console.rule()
            if message.lower() == "/bye":
                self.system.send_message("Exiting the program")
                return
            self.ai.query(message)


if __name__ == "__main__":
    TerminalDemo().run()
