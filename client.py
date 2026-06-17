from openai import OpenAI
client = OpenAI(
  api_key="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",
)
completion = client.chat.completions.create(
  model="gpt-5.5",
  messages=[
    {"role": "system", "content": "You are a virtual assistant named jarvis skilled in general tasks like Alexa and Google Cloud"},
    {"role": "user", "content": "what is coding"}
  ]
)
print(completion.choices[0].message.content)