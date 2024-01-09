from typing import Tuple

from langchain import PromptTemplate
from langchain.chains import LLMChain
from langchain.chat_models import ChatOpenAI

from agents import lookup
from outpur_parsers import pydantic_output_parser as pos
from tools import scrape_linikedin_profile
from utils import load_prompt_raw

MODEL_NAME = "mistralai/Mixtral-8x7B-Instruct-v0.1"


def get_information(name: str) -> Tuple[str, str]:
    llm = ChatOpenAI(temperature=0, model_name=MODEL_NAME)

    urn_id = lookup("Morteza Hosseini University of Calgary", llm=llm)

    summary_prompt_template = PromptTemplate(
        input_variables=["information"],
        template=load_prompt_raw("summary.txt"),
        partial_variables={
            "format_instructions": pos.get_format_instructions()
        },
    )

    chain = LLMChain(llm=llm, prompt=summary_prompt_template)

    linkedin_data, photo = scrape_linikedin_profile(urn_id)

    return (pos.parse(chain.run(information=linkedin_data)), photo)


if __name__ == "__main__":
    print(get_information("Seyed Morteza Hosseini Ucalgary"))
