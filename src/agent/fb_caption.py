from langchain_core.prompts import ChatPromptTemplate

from .llama import LLAMAAgent


class FacebookCaptionAgent(LLAMAAgent):
    @property
    def prompt_template(self) -> ChatPromptTemplate:
        return ChatPromptTemplate.from_messages(
            [
                (
                    "system",
                    """You are an AI agent with expertise in summary.\n
                 You will be given an article summary and you should provide several Facebook captions according to the summary. \n""",
                ),
                ("user", "{input} \n"),
            ],
        )
