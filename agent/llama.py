from langchain_community.chat_models import ChatOllama
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnableSerializable


class LLAMAAgent:
    def __init__(self) -> None:
        self.__llm: ChatOllama = ChatOllama(model="llama3")

    @property
    def prompt_template(self) -> ChatPromptTemplate:
        raise NotImplementedError()

    def invoke(self, message: str) -> str:
        return self.__get_runnable().invoke(self._create_input(message))

    def __get_runnable(self) -> RunnableSerializable:
        return self.prompt_template | self.__llm | StrOutputParser()

    def _create_input(self, message: str) -> dict:
        return {"input": message}
