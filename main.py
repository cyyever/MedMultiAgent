# -*- coding: utf-8 -*-
import datetime
from typing import Literal

import typer

from cli import CliApp
from session import State

entry_point = typer.Typer()
session_id = datetime.datetime.now().strftime("%Y%m%d%H%M%S")

state = None


def initialize_session_state(at: Literal["web", "cli"]) -> None:
    global state
    if state is None:
        state = State(at)


@entry_point.command(help="Start the CLI application.")
def cli() -> None:
    initialize_session_state("cli")
    cli_app = CliApp()
    cli_app.run()


if __name__ == "__main__":
    entry_point()
