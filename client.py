from openai import OpenAI
client = OpenAI(
  api_key="my-api-key",
)
completion = client.chat.completions.create(
  model="gpt-5.5",
  messages=[
    {"role": "system", "content": "You are a virtual assistant named jarvis skilled in general tasks like Alexa and Google Cloud"},
    {"role": "user", "content": "what is coding"}
  ]
)
print(completion.choices[0].message.content)
