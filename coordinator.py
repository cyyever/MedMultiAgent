from typing import Any

from agent import DoctorAgent


class Coordinator:
    def __init__(self) -> None:
        self.doctor = DoctorAgent()

    def invoke(self, message: str) -> Any:
        return self.doctor.invoke(message=message)
