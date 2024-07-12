from agent import DoctorAgent, FacebookCaptionAgent


class Coordinator:
    def __init__(self) -> None:
        self.default_agent = DoctorAgent
        self.agent = FacebookCaptionAgent()

    def invoke(self, message: str) -> str:
        return self.agent.invoke(message=message)
