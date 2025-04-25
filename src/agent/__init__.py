from enum import StrEnum, auto
from typing import Any

from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnableSerializable
from langchain_ollama import ChatOllama


class OllamaAgent:
    def __init__(self, model_name: str) -> None:
        self.__llm = ChatOllama(model=model_name)

    @property
    def prompt_template(self) -> ChatPromptTemplate:
        raise NotImplementedError()

    def invoke(self, message: str) -> str:
        return self.__get_runnable().invoke({"input": message})

    def __get_runnable(self) -> RunnableSerializable:
        return self.prompt_template | self.__llm | StrOutputParser()


class Role(StrEnum):
    Doctor = auto()
    FacebookCaption = auto()
    PaperReviewer = auto()
    JobSkill = auto()
    EnglishLyricist = auto()
    ChineseLyricist = auto()


class PredefinedAgent(OllamaAgent):
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
        Role.EnglishLyricist: (
            "system",
            """You are a professional lyricist.\n
                 You will be given a subject and you should output a lyrics accordingly. \n""",
        ),
        Role.PaperReviewer: (
            "system",
            """You are an AI agent with expertise in English academic writing.\n
                 You will be given the content of a academic paper written in LaTeX and you should check English syntactic and grammatical errors in the paper. \n""",
        ),
        Role.ChineseLyricist: (
            "system",
            """你擅长写歌词.\n
                你会被给定一个主题，依据这个主题写一份歌词. \n""",
        ),
    }
    models: dict[Role, str] = {}

    def __init__(self, role: Role, model_name: str | None = None) -> None:
        if model_name is None:
            model_name = self.models.get(role, "deepseek-r1:8b")
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
