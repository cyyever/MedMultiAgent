from langchain_community.chat_models import ChatOllama
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnableSerializable


class ConsultAgent:
    def __init__(self) -> None:
        self.llm: ChatOllama = ChatOllama(model="llama3")
        self.prompt_template = ChatPromptTemplate.from_messages(
            [
                (
                    "system",
                    """You are an AI assistant
                 with expertise in medical diagnosis.\n
                 You will be given a medical question from an user and you
                 should provide your answer. \n""",
                ),
                ("user", "{medical_question} \n"),
            ],
        )

    def get_runnable(self) -> RunnableSerializable:
        return self.prompt_template | self.llm | StrOutputParser()
