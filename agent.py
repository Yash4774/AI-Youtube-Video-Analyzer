from agno.agent import Agent

from agno.models.openai import OpenAIResponses
from agno.models.groq import Groq

from dotenv import load_dotenv
import os
from agno.tools.wikipedia import WikipediaTools


load_dotenv()
def build_agent():
    return Agent(

        model=Groq(id="qwen/qwen3-32b",
            

        
        ),
        tools=([WikipediaTools()]),
        markdown=True,
        instructions="You are a Helpful and expert travel agent.",
        add_datetime_to_context=True
    )

agent = build_agent()

agent.print_response("Who Is Baahubali Actor?")
