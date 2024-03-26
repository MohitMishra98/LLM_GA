from openai import OpenAI
import json

client = OpenAI()

prompt = "set the temprature to 300 kelvin"

temperature=1
room_number=0


#this function is used to set the temprature of a specific value in specific room
def set_temp(temp:int,room:int):
    global temperature,room_number
    temperature = temp
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
        "room_number": {
          "type": "integer",
          "description": "The room number to set the temperature in"
        }
      },
      "required": ["temperature", "room_number"]
    }
  }
}
]
)
#use tools to convert any function into this format by giving some examples

print(completion)

#visit https://platform.openai.com/docs/api-reference/chat/object to see the structuring of data
arguments_json = json.loads(completion.choices[0].message.tool_calls[0].function.arguments)

function_name = completion.choices[0].message.tool_calls[0].function.name

print(temperature,room_number)

if function_name == "set_temp":
    set_temp(int(arguments_json["temperature"]),int(arguments_json["room_number"]))

print(temperature,room_number)