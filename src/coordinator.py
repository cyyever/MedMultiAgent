import os
from agent import PredefinedAgent, Role


class Coordinator:
    def __init__(self) -> None:
        role = os.getenv("AGENT_ROLE")
        if role is not None:
            for r in Role:
                if r.lower() == role.lower():
                    default_role = r
                    self.agent = PredefinedAgent(role=default_role)
                    return
            raise RuntimeError(f"invalid role {role}")
        self.agent = PredefinedAgent(role=Role.Doctor)

    def invoke(self, message: str) -> str:
        return self.agent.invoke(message=message)
