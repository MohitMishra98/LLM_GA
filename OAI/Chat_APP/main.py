from openai import OpenAI

client = OpenAI()

messages = [{"role":"system","content":"You are a helpful assistant"}]

completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages = messages
)

while True:
    prompt = input("Enter your prompt here : ")

    if not prompt:
        break

    messages.append({"role":"user","content":prompt})

    completion = client.chat.completions.create(model="gpt-3.5-turbo",messages = messages)

    messages.append({"role":"assistant","content":completion.choices[0].message.content})

    print(completion.choices[0].message.content)