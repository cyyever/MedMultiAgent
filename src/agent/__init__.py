from enum import StrEnum, auto
from typing import Any

from langchain_core.prompts import ChatPromptTemplate

from .llama import LLAMAAgent


class Role(StrEnum):
    Doctor = auto()
    FacebookCaption = auto()
    JobSkill = auto()
    ChineseLyricist = auto()


class PredefinedAgent(LLAMAAgent):
    templates: dict[Role, Any] = {
        Role.Doctor: (
            "system",
            """You are an AI doctor with expertise in medical diagnosis.\n
                 You will be given a medical question from a patient and you should provide your answer. \n""",
        ),
        Role.FacebookCaption: (
            "system",
            """You are an AI agent with expertise in article summary.\n
                 You will be given an article and you should provide several Facebook captions of the article. \n""",
        ),
        Role.JobSkill: (
            "system",
            """You are an AI agent with expertise in AI job skills.\n
                 You will be given some questions about AI job skills and you should provide useful advise. \n""",
        ),
        Role.ChineseLyricist: (
            "system",
            """你擅长写歌词.\n
                你会被给定一个主题，依据这个主题写一份歌词. \n""",
        ),
    }
    models: dict[Role, str] = {Role.ChineseLyricist: "llama2-chinese"}

    def __init__(self, role: Role, model_name: str | None = None) -> None:
        if model_name is None:
            model_name = self.models.get(role, "llama3")
        super().__init__(model_name=model_name)
        self.__role = role

    @property
    def prompt_template(self) -> ChatPromptTemplate:
        return ChatPromptTemplate.from_messages(
            [
                self.templates[self.__role],
                ("user", "{input} \n"),
            ],
        )


__all__ = ["PredefinedAgent", "Role"]
