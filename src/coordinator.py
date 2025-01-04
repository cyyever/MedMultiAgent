import os
from agent import PredefinedAgent, Role


class Coordinator:
    def __init__(self, role: Role | None = None) -> None:
        if role is None:
            role_str = os.getenv("AGENT_ROLE")
            if role_str is not None:
                for r in Role:
                    if r.lower() == role_str.lower():
                        self.agent = PredefinedAgent(role=r)
                        return
                raise RuntimeError(f"invalid role {role}")
        if role is None:
            role = Role.Doctor
        self.agent = PredefinedAgent(role=role)

    def invoke(self, message: str) -> str:
        return self.agent.invoke(message=message)


if __name__ == "__main__":
    coordinator = Coordinator(role=Role.ChineseLyricist)
    for i in range(1, 100):
        output = coordinator.invoke(
            message="为小学生成校歌歌词，字数在五十字到七十字之间，需要包含爱国元素"
        )
        with open(f"lyricist_{i}.txt", encoding="utf8") as f:
            f.write(output)
