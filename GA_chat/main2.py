##creating a conversation bot

import google.generativeai as genai
import os

#this is to fetch api key from environment variable
#use given command with export to set the environment variable no "" of key
#export GOOGLE_API_KEY=your_api_key
GOOGLE_API_KEY = os.environ.get("GOOGLE_API_KEY")

#configuring api key

genai.configure(api_key=GOOGLE_API_KEY)

#generate text from text inputs

#creates a object "model" using class "GenerativeModel" from "genai" library

safety_settings = [
  {
    "category": "HARM_CATEGORY_HARASSMENT",
    "threshold": "BLOCK_NONE"
  },
  {
    "category": "HARM_CATEGORY_HATE_SPEECH",
    "threshold": "BLOCK_NONE"
  },
  {
    "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
    "threshold": "BLOCK_NONE"
  },
  {
    "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
    "threshold": "BLOCK_NONE"
  },
]

model = genai.GenerativeModel(model_name="gemini-1.5-pro-latest",
                              safety_settings=safety_settings,
                              system_instruction="You are a cat. Your name is Neko.")

#handling chats from raw api
#this method is more effective

#structure of the conversion list will be like this
messages = [{"role":"user","parts":["user message1"]},
            {"role":"model","parts":["model message1"]},
            {"role":"user","parts":["user message2"]},
            {"role":"model","parts":["user message2"]},]
#specifically use this structre otherwise it will not work

messages = []

while True:
    #taking input from user
    new_prompt = input()
    if(new_prompt=="AAAA"):
        break
    #adding user message of the conversation list
    messages.append({"role":"user","parts":[new_prompt]})
    #generating model response by provideing list
    response = model.generate_content(messages)
    #adding model message of the conversation list
    messages.append({"role":"model","parts":[response.text]})
    #printing response to the user
    print(response.text)

print(messages)

#works perfectly
print("this is for loop")
for i in messages:
    print(f"{i["role"]} : {i["parts"][0]}")

#working of this for loop

"""
"i" will give the firts "dict"
we will access the "key" "role"
which will provide the value of that key

now we will access the "key" "parts"
which will provide us a "value"
it will be a list
we will access the 0 index of this list by [0]

now for loop will move and i will be the 1 index of list "messages"
"""