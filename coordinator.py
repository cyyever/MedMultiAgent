# -*- coding: utf-8 -*-
from typing import AsyncIterator

from workflow import ConsultOpenAIGPT4


# Just for testing
# Not the final version
class Coordinator:
    def __init__(self) -> None:
        pass

    async def start_with(
        self,
        message: str,
    ) -> AsyncIterator:
        workflow = ConsultOpenAIGPT4().get_runnable()
        return workflow.astream(message)
