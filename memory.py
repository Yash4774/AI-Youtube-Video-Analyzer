from agno.agent import Agent
from agno.models.groq import Groq
from dotenv import load_dotenv
import os
from agno.db.sqlite import SqliteDb
from rich.pretty import pprint




load_dotenv()

db = SqliteDb(db_file="agno.db")
db.clear_memories()


def build_agent():
    return Agent(
        db=db,
        model=Groq(id="qwen/qwen3-32b",
            

        
        ),
        markdown=True,
        instructions="You are a Helpful and expert travel agent.",
        add_datetime_to_context=True,
        add_history_to_context=True,
        enable_user_memories=True
    )

agent = build_agent()
user_id = "yash@gmail.com"

agent.print_response("I am Yash & I am a Data Scientist.", user_id=user_id)
agent.print_response("Who Am I?", user_id=user_id)

print("MEMORIES: ")

memories = agent.get_user_memories(
    user_id=user_id
)

pprint(memories)


