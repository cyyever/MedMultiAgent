from typing import Any, Iterator

from langchain_community.chat_models import ChatOllama
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnableSerializable


class DoctorAgent:
    def __init__(self) -> None:
        self.llm: ChatOllama = ChatOllama(model="llama3")
        self.prompt_template = ChatPromptTemplate.from_messages(
            [
                (
                    "system",
                    """You are an AI doctor
                 with expertise in medical diagnosis.\n
                 You will be given a medical question from an user and you
                 should provide your answer. \n""",
                ),
                ("user", "{medical_question} \n"),
            ],
        )

    def invoke(self, message: str) -> Any:
        return self.__get_runnable().invoke(self.__create_input(message))

    def stream(self, message: str) -> Iterator:
        return self.__get_runnable().stream(self.__create_input(message))

    def __get_runnable(self) -> RunnableSerializable:
        return self.prompt_template | self.llm | StrOutputParser()

    def __create_input(self, message: str) -> dict:
        return {"medical_question": message}
