import os
from autogen import ConversableAgent

#creating a agent

agent = ConversableAgent(
    "chatbot",
    llm_config={"config_list": [{"model": "gpt-3.5-turbo", "api_key": os.environ.get("OPENAI_API_KEY")}]},
    code_execution_config=False,  # Turn off code execution, by default it is off.
    function_map=None,  # No registered functions, by default it is None.
    human_input_mode="NEVER",  # Never ask for human input.
)

reply = agent.generate_reply(messages=[{"role":"user" , "content" : "what is autogen"}])
#       agentNameFrom.generate_reply(agentNameTo,messages)

print(reply)