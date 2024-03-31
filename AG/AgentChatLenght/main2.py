import os
from autogen import ConversableAgent

# controlling length of conversations Using max_consecutive_auto_reply

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
    max_consecutive_auto_reply=1 # by using this arument joe can only reply 1
)

response = joe.initiate_chat(cathy,message="prompt is new")

# in the response joe messages is 2 because 1 is initiated meaasge and 1 is reply
# reply is only 1