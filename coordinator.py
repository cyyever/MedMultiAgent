from agent import DoctorAgent, JobSkillAgent


class Coordinator:
    def __init__(self) -> None:
        self.default_agent = DoctorAgent()
        self.agent = JobSkillAgent()

    def invoke(self, message: str) -> str:
        return self.agent.invoke(message=message)
