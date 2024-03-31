import os
from autogen import ConversableAgent

# using human_input_mode="TERMINATE"

# asks for human input when the chat termination condition is met

# In this mode, human input is only requested when a termination condition is met.
# If the human choose to intercept and reply, the counter will be reset; 
# if the human choose to skip, automatic reply mechanism will be used; if the human choose to terminate, 
# the conversation will be terminated.

llm_config = {"config_list": [{"model": "gpt-3.5-turbo", "temperature": 0.9, "api_key": os.environ.get("OPENAI_API_KEY")}]}

agent_with_number = ConversableAgent(
    "agent_with_number",
    system_message="""You are playing a game of guess-my-number. 
        You have the number 999 in your mind, and I will try to guess it. 
        "If I guess too high, say 'too high', if I guess too low, say 'too low'. 
        Do not say anything else """,
    llm_config=llm_config,
    is_termination_msg=lambda msg: "999" in msg["content"],  # terminate if the number is guessed by the other agent
    human_input_mode="TERMINATE",  # ask for human input when the game is terminated
)

agent_guess_number = ConversableAgent(
    "agent_guess_number",
    system_message="I have a number in my mind, and you will try to guess it. "
    "If I say 'too high', you should guess a lower number. If I say 'too low', "
    "you should guess a higher number. ",
    llm_config=llm_config,
    human_input_mode="NEVER",
)

response = agent_guess_number.initiate_chat(agent_with_number,message="995")