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
model = genai.GenerativeModel("gemini-1.0-pro")

print(type(model))

#starting chat
#we can use this feature using start_chat method


chat = model.start_chat(history=[])

#here "chat" is a "ChatSession"
#we can make multiple chats at same time using multiple ChatSession names
#like chat1 = model.start_chat(history=[])


#uncomment this
"""
response = chat.send_message("Hello")
print(response.text)

response = chat.send_message("what can you do")
print(response.text)

response = chat.send_message("write features of vscode")
print(response.text)

response = chat.send_message("summarize this conversation")
print(response.text)
"""

#this response will be in same format as in normal text

response = chat.send_message("Hmmmmmmmmm")
print(response.text)

#send_message method sends the message to the model
#this also adds the message and response to the history

#streaming response

response = chat.send_message("explain gemini pro in a long paragraph",stream=True)

for chunk in response:
    print(chunk.text)

#to print chat history
for message in chat.history:
  print(f'**{message.role}**: {message.parts[0].text}')


#to get chat history in a string
#uncomment this
"""
hist = ""

for message in chat.history:
  hist += str(f'**{message.role}**: {message.parts[0].text}\n')

print(hist)
"""
print(chat.history)