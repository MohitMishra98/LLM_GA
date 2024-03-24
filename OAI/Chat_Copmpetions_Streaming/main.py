from openai import OpenAI


client = OpenAI()

completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "You are a poetic assistant, skilled in explaining complex programming concepts with creative flair."},
    {"role": "user", "content": "say hi"}
  ],
  stream=True
)

for chunk in completion:
    print(chunk.choices[0].delta.content,end="")

