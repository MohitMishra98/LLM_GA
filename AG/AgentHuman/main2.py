import os
from autogen import ConversableAgent

# by using human_input_mode="ALWAYS" human_proxy agent will always ask for our response and then send
# it to other agent

llm_config = {"config_list": [{"model": "gpt-3.5-turbo", "temperature": 0.9, "api_key": os.environ.get("OPENAI_API_KEY")}]}

agent_with_number = ConversableAgent(
    "agent_with_number",
    system_message="""You are playing a game of guess-my-number. 
        You have the number 999 in your mind, and I will try to guess it. 
        "If I guess too high, say 'too high', if I guess too low, say 'too low'. 
        Do not say anything else """,
    llm_config=llm_config,
    is_termination_msg=lambda msg: "999" in msg["content"],  # terminate if the number is guessed by the other agent
    human_input_mode="NEVER",  # never ask for human input
)

human_proxy = ConversableAgent(
    "human_proxy",
    llm_config=False,  # no LLM used for human proxy
    human_input_mode="ALWAYS",  # always ask for human input
)

response = human_proxy.initiate_chat(agent_with_number,message="10")