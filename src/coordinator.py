from agent import PredefinedAgent, Role


class Coordinator:
    def __init__(self) -> None:
        self.agent = PredefinedAgent(role=Role.Doctor)

    def invoke(self, message: str) -> str:
        return self.agent.invoke(message=message)
