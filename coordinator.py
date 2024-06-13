from typing import Iterator

from agent import DoctorAgent


class Coordinator:
    def __init__(self) -> None:
        self.doctor = DoctorAgent()

    def stream(self, message: str) -> Iterator:
        return self.doctor.get_runnable().stream(message)
