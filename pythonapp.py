import google.generativeai as genai
import os

#this is to fetch api key from environment variable
#use given command with export to set the environment variable no "" of key
#export GOOGLE_API_KEY=your_api_key
GOOGLE_API_KEY = os.environ.get("GOOGLE_API_KEY")

#configuring api key

genai.configure(api_key=GOOGLE_API_KEY)

for m in genai.list_models():
  if 'generateContent' in m.supported_generation_methods:
    print(m.name)

#generate text from text inputs

#creates a object "model" using class "GenerativeModel" from "genai" library
model = genai.GenerativeModel("gemini-1.0-pro")

print(type(model))



#generate_content() is a method of class "GenerativeModel"
response = model.generate_content("say hello in hindi")

print(response.text)
print(type(response))


"""
#response object have following attributes



response.prompt_feedback
for safety settings 


response.candidates
for possible outputs
"""

#streaming response

response = model.generate_content("write a paragraph about LLM",stream=True)

for chunk in response:
  print(chunk.text)

#uses a for loop to iterate through the response object and print each chunk of text.
#chunk is equivalent to "i"
#response is equivalent to range(0,10)
#.text is attribute of object chunk
#note that every chunk will be printed on a seperate line

