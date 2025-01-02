from langchain_core.prompts import ChatPromptTemplate

from .llama import LLAMAAgent


class DoctorAgent(LLAMAAgent):
    @property
    def prompt_template(self) -> ChatPromptTemplate:
        return ChatPromptTemplate.from_messages(
            [
                (
                    "system",
                    """You are an AI doctor
                 with expertise in medical diagnosis.\n
                 You will be given a medical question from a patient and you
                 should provide your answer. \n""",
                ),
                ("user", "{input} \n"),
            ],
        )
