# -*- coding: utf-8 -*-
from abc import ABC, abstractmethod

from langchain_community.chat_models import ChatOllama
from langchain_core.messages import HumanMessage
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.pydantic_v1 import BaseModel, Field
from langchain_core.runnables import Runnable
from langchain_openai import ChatOpenAI

from utils import auto_schema_prompt


class Workflow(ABC):
    description: str

    @abstractmethod
    def get_runnable(self) -> Runnable:
        pass


# LLM involved Runnable as a workflow
class ConsultCodellama(Workflow):
    def __init__(self):
        class CodeFeedback(BaseModel):
            feedback: str = Field(..., description="the feedback of the code")
            score: float = Field(
                ...,
                description="""Your rating of the code
                                  from 0 to 10""",
            )

        self.llm = ChatOllama(model="codellama")
        self.prompt_template = ChatPromptTemplate.from_messages(
            [
                (
                    "system",
                    """You are a AI assitant
                 with expertise in code review.\n
                 You will be given a code snippet and you
                 should provide your feedback and rating on the code. \n
                 {output_prompt} \n""",
                ),
                ("user", "{code_snippet} \n"),
            ],
        )
        try:
            self.llm = self.llm.with_structured_output(CodeFeedback)
        except NotImplementedError:
            output_prompt, output_parser = auto_schema_prompt(CodeFeedback)
            self.prompt_template = self.prompt_template.partial(
                output_prompt=output_prompt,
            )
            self.llm = self.llm | output_parser
        self.description = """Consult Codellama for code review.\n
        Codellama is an AI assistant specialized in code review.
        It will provide comments and rating on the code snippet."""

    def get_runnable(self):
        return self.prompt_template | self.llm


class ConsultOpenAIGPT4(Workflow):
    def __init__(self):
        self.llm = ChatOpenAI(model="gpt-4-turbo")
        self.description = """Consult the most intelligent
                              AI model GPT-4 for your questions.\n"""

        self.prompt = ChatPromptTemplate.from_messages(
            messages=[HumanMessage(content="{userinput}")],
        )
        self.runnable = self.llm | StrOutputParser()

    def get_runnable(self):
        return self.runnable
