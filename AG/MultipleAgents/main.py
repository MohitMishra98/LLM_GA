import os
from autogen import ConversableAgent

llm_config = {"config_list": [{"model": "gpt-3.5-turbo", "temperature": 0.9, "api_key": os.environ.get("OPENAI_API_KEY")}]}

cathy = ConversableAgent(
    "cathy",
    system_message="Your name is Cathy and you are a part of a duo of comedians.",
    llm_config=llm_config,
    human_input_mode="NEVER",  # Never ask for human input.
)

joe = ConversableAgent(
    "joe",
    system_message="Your name is Joe and you are a part of a duo of comedians.",
    llm_config=llm_config,
    human_input_mode="NEVER",  # Never ask for human input.
)

response = joe.initiate_chat(cathy,message="Cathy, tell me a joke.",max_turns=10)

#          agentNameFrom.initiate_chat(AgentNameTo,message="prompt",mat_turns=2)

print(response)