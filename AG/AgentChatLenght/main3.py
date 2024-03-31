import os
from autogen import ConversableAgent

# controlling chat length Using is_termination_msg

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
    is_termination_msg=lambda msg: "aaaa" in msg["content"].lower(),
    # by using this argument whenever other agent reply to this agent and the message contains
    # AAAA chat will stop
)

response = joe.initiate_chat(cathy, message="Cathy, tell me a joke and then say the words AAAA.")