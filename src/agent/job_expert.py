from langchain_core.prompts import ChatPromptTemplate

from .llama import LLAMAAgent


class JobSkillAgent(LLAMAAgent):
    @property
    def prompt_template(self) -> ChatPromptTemplate:
        return ChatPromptTemplate.from_messages(
            [
                (
                    "system",
                    """You are an AI agent
                 with expertise in AI job skills.\n
                 You will be given some questions about AI job skills and you
                 should provide useful advise. \n""",
                ),
                ("user", "{input} \n"),
            ],
        )
