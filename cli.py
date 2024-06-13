# -*- coding: utf-8 -*-
import re
from typing import Iterator

from loguru import logger
from rich.console import Console
from rich.live import Live
from rich.panel import Panel

from coordinator import Coordinator

console = Console()


class Entity:
    prefix = "No prefix"

    def send_message(self, message: str) -> None:
        console.print(f"{self.prefix} {message}")


class System(Entity):
    prefix = ":gear: [bold green]System:[/bold green]"


class AI(Entity):
    prefix = ":robot: [bold magenta]AI:[/bold magenta]"

    def send_stream_message(self, message_generator: Iterator) -> None:

        def create_completed_panel(message: str):
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

        typed_message = ""
        with Live(console=console, refresh_per_second=10) as live:
            for char in message_generator:
                print(char)
                typed_message += char
                live.update(typed_message)
            live.update(create_completed_panel(typed_message))


class CliApp:
    def __init__(self):
        self.ai = AI()
        self.system = System()
        self.coordinator = Coordinator()

    def prompt_loop(self) -> None:
        self.system.send_message("Medical Multi Agent initialized")
        self.system.send_message(
            "Type '/file <file_path>' followed by a url to pass a file to the AI agent",
        )
        self.system.send_message("Type '/bye' to exit the program")
        while True:
            self.system.send_message("Enter your questions or commands:")
            message = input(
                ">>> ",
            ).strip()  # Using plain input to get user input
            console.rule()
            if re.search(r"/bye", message, re.IGNORECASE):
                self.system.send_message("Exiting the program")
                return
            if match := re.search(
                r"/file (\w+)",
                message,
                re.IGNORECASE,
            ):
                file_path = match.group(1).strip()
                self.system.send_message(f"File path: {file_path}")
                logger.info(f"User upload a file: {file_path}")
            self.ai.send_stream_message(self.coordinator.stream(message))


if __name__ == "__main__":
    CliApp().prompt_loop()
