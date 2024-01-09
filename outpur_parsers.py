from typing import List

from langchain.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field


class PersonInformation(BaseModel):
    summary: str = Field(description="Summary of the person")
    facts: List[str] = Field(description="Intresting facts about the person")
    topics: List[str] = Field(description="Topics that may intrest the person")
    icebreakers: List[str] = Field(
        description="Ice breakers to open the conversation with the person"
    )


pydantic_output_parser = PydanticOutputParser(
    pydantic_object=PersonInformation
)
