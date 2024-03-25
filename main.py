from openai import OpenAI
import json

client = OpenAI()

prompt = "set the temprature to 300 kelvin"

#this function is used to set the temprature of a specific value in specific room
def set_temp(temp:int,room:int):
    global temprature,room_number
    temprature = temp
    room_number = room




completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[{"role":"system","content":"You are a helpful assistant"},
              {"role":"user","content":prompt}],
    tools = [{
  "type": "function",
  "function": {
    "name": "set_temp",
    "description": "Set the temperature of a specific value in a specific room",
    "parameters": {
      "type": "object",
      "properties": {
        "temperature": {
          "type": "integer",
          "description": "The temperature value to set"
        },
        "room": {
          "type": "integer",
          "description": "The room number to set the temperature in"
        }
      },
      "required": ["temperature", "room"]
    }
  }
}
]
)

#visit https://platform.openai.com/docs/api-reference/chat/object to see the structuring of data

var1 = completion.choices[0].message.tool_calls[0].function.arguments
var2 = completion.choices[0].message.tool_calls[0].function.name

print(var1)
print(var2)

print(completion)

completion_json = json.loads(completion.choices[0].message.tool_calls[0].function.arguments)
print(completion_json["temperature"])
#creating a function to call function