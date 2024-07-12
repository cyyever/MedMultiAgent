from langchain_community.chat_models import ChatOllama
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnableSerializable


class FacebookCaptionAgent:
    def __init__(self) -> None:
        self.llm: ChatOllama = ChatOllama(model="llama3")
        self.prompt_template = ChatPromptTemplate.from_messages(
            [
                (
                    "system",
                    """You are an AI agent
                 with expertise in summary.\n
                 You will be given an article summary and you
                 should provide several Facebook captions according to the summary. \n""",
                ),
                ("user", "{phrase} \n"),
            ],
        )

    def invoke(self, message: str) -> str:
        return self.__get_runnable().invoke(self.__create_input(message))

    def __get_runnable(self) -> RunnableSerializable:
        return self.prompt_template | self.llm | StrOutputParser()

    def __create_input(self, message: str) -> dict:
        return {"phrase": message}
