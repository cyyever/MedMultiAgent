from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnableSerializable
from langchain_ollama import ChatOllama


class LLAMAAgent:
    def __init__(self, model_name: str) -> None:
        self.__llm: ChatOllama = ChatOllama(model=model_name)

    @property
    def prompt_template(self) -> ChatPromptTemplate:
        raise NotImplementedError()

    def invoke(self, message: str) -> str:
        return self.__get_runnable().invoke({"input": message})

    def __get_runnable(self) -> RunnableSerializable:
        return self.prompt_template | self.__llm | StrOutputParser()
