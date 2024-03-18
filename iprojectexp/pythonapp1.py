import os
from crewai import Agent, Task, Crew, Process
from langchain_community.chat_models import ChatCohere
from langchain.tools import DuckDuckGoSearchRun
from langchain.agents import load_tools

search_tool = DuckDuckGoSearchRun() #enabling the agents to have access to the internet

os.environ["COHERE_API_KEY"] = "COHERE_API_KEY"
# Initiate our LLM chat model from Cohere
llm=ChatCohere(temperature=0.3)

# Define your agents with roles and goals
researcher = Agent(
  role='Senior Research Analyst',
  goal='Uncover real use cases of generative AI applied across charity organisations., search the internet to identifying real-life use cases,',
  backstory="""You are a Senior Research Analyst at a leading tech think tank.

Your expertise lies in identifying emerging trends and technologies in generative ai, identifying real-world use cases and providing the organisation name (you must know the actual company name), how they have applied it and the benefits they are experiencing.

You have a knack for dissecting complex data and presenting actionable insights.""",
  verbose=True,
  allow_delegation=False,
  llm=llm,
  tools=[search_tool])

task1 = Task(
  description="""Conduct a comprehensive analysis of the latest use cases of generative AI applied across charity organisations. Search the internet to identifying real-life use cases’

Identifying real-world use cases and providing the organisation name(you must know the actual company name), how they have applied it and the benefits they are experiencing. Compile your findings in a detailed report.

Your final answer MUST be a full analysis report containing the full details of the generative ai use cases.""",
  agent=researcher
)

writer = Agent(
  role='Tech Content Strategist',
  goal='Craft compelling content on tech advancements',
  backstory="""You are a renowned Tech Content Strategist, known for your insightful and engaging articles on technology and innovation. With a deep understanding of the tech industry, you transform complex concepts into compelling narratives.""",
  verbose=True,
  allow_delegation=False,
  llm=llm,
  # Passing search and human tools to the agent
  tools=[search_tool]
)

task2 = Task(
  description="""Using the insights from the researcher’s report, develop an engaging blog post that highlights the most significant AI advancements. , search the internet to validate the real-life use cases.

Report on real-world use cases and provide the organisation name, how they have applied it and the benefits they are experiencing. Your post should be informative yet accessible, catering to a tech-savvy audience.

Aim for a narrative that captures the essence of these breakthroughs and their implications for the future.

Your final answer MUST be the full blog post of at least 5 paragraphs.""",
  agent=writer
)

# Instantiate your crew with a sequential process
crew = Crew(
  agents=[researcher, writer],
  tasks=[task1, task2],
  verbose=1
)

# Get your crew to work!
result = crew.kickoff()

print("######################")
print(result)