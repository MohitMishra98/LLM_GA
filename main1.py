import os
from autogen import ConversableAgent
from typing import Annotated, Literal

llm_config = {"config_list": [{"model": "gpt-3.5-turbo", "temperature": 0.9, "api_key": os.environ.get("OPENAI_API_KEY")}]}

Operator = Literal["+", "-", "*", "/"]


def calculator(a: int, b: int, operator: Annotated[Operator, "operator"]) -> int:
    if operator == "+":
        return a + b
    elif operator == "-":
        return a - b
    elif operator == "*":
        return a * b
    elif operator == "/":
        return int(a / b)
    else:
        raise ValueError("Invalid operator")

# Registering tools

# Let's first define the assistant agent that suggests tool calls.
assistant = ConversableAgent(
    name="Assistant",
    system_message="You are a helpful AI assistant. "
    "You can help with simple calculations. "
    "Return 'TERMINATE' when the task is done.",
    llm_config=llm_config,
)

# The user proxy agent is used for interacting with the assistant agent
# and executes tool calls.
user_proxy = ConversableAgent(
    name="User",
    llm_config=False,
    is_termination_msg=lambda msg: msg.get("content") is not None and "TERMINATE" in msg["content"],
    human_input_mode="NEVER",
)

# Register the tool signature with the assistant agent.
# By doing this the agent knows about this tool exist and it can call it (for calling)
assistant.register_for_llm(name="calculator", description="A simple calculator")(calculator)

# Register the tool function with the user proxy agent.
# By doing this this agent can use this tools and provide output based on the call  (for executing call)
user_proxy.register_for_execution(name="calculator")(calculator)

response = user_proxy.initiate_chat(assistant, message="What is (1423 - 123) / 3 + (32 + 23) * 5?")

print(response)