from openai import OpenAI
client = OpenAI(
    api_key= "your-key"
)

chat_completion = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[{"role": "user", "content": "Hello, ChatGPT!"}]
)

response = chat_completion.choices[0].message.content
print(response)
