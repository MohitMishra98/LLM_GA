import google.generativeai as genai
import os
import PIL.Image

#this is to fetch api key from environment variable
#use given command with export to set the environment variable no "" of key
#export GOOGLE_API_KEY=your_api_key
GOOGLE_API_KEY = os.environ.get("GOOGLE_API_KEY")

#configuring api key

genai.configure(api_key=GOOGLE_API_KEY)

#to print the list of available models
for m in genai.list_models():
  if 'generateContent' in m.supported_generation_methods:
    print(m.name)



#generate text from text inputs

#creates a object "model" using class "GenerativeModel" from "genai" library
model = genai.GenerativeModel("gemini-1.0-pro-vision-latest")

#generating text from text and image

#loading image
image = PIL.Image.open('/workspaces/LLM_GA/image.jpg')

#to pass an image provide a "list" with "text",image
#["text",image]
response = model.generate_content(["write description of this image",image])


print(response.text)

#streaning response

response = model.generate_content(["write description of this image",image],stream=True)

for chunk in response:
  print(chunk.text)

