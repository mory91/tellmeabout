from langchain import PromptTemplate
from langchain.agents import AgentType, Tool, initialize_agent
from langchain.chat_models import ChatOpenAI

from tools import search_poeple
from utils import load_prompt_raw


def lookup(name: str, llm: ChatOpenAI) -> str:
    search_people_tool = Tool(
        name=(
            "Search linkedin for a given name"
            " and returns the found users data."
        ),
        func=search_poeple,
        description=(
            "Useful for when you need get the linkedin urn_id of a person."
        ),
    )
    tools = (search_people_tool,)

    agent = initialize_agent(
        tools=tools,
        llm=llm,
        agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
        verbose=True,
    )

    prompt_template = PromptTemplate(
        template=load_prompt_raw("linkedin_lookup.txt"),
        input_variables=["name_of_person"],
    )

    linkedin_profile_url = agent.run(
        prompt_template.format_prompt(name_of_person=name)
    )

    return linkedin_profile_url
