import os
from autogen import ConversableAgent

# by setting human_input_mode="NEVER" it will never ask for human input

llm_config = {"config_list": [{"model": "gpt-3.5-turbo", "temperature": 0.9, "api_key": os.environ.get("OPENAI_API_KEY")}]}

agent_with_number = ConversableAgent(
    "agent_with_number",
    system_message="""You are playing a game of guess-my-number. 
        You have the number 53 in your mind, and I will try to guess it. 
        "If I guess too high, say 'too high', if I guess too low, say 'too low'. 
        Do not say anything else """,
    llm_config=llm_config,
    is_termination_msg=lambda msg: "53" in msg["content"],  # terminate if the number is guessed by the other agent
    human_input_mode="NEVER",  # never ask for human input
)

agent_guess_number = ConversableAgent(
    "agent_guess_number",
    system_message="I have a number in my mind, and you will try to guess it. "
    "If I say 'too high', you should guess a lower number. If I say 'too low', "
    "you should guess a higher number. ",
    llm_config=llm_config,
    human_input_mode="NEVER", # never ask for human input
)

response = agent_with_number.initiate_chat(agent_guess_number,message="I have a number between 1 and 100. Guess it!")