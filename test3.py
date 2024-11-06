from openai import OpenAI
client = OpenAI(
    api_key= "your-key"
)

chat_completion = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": "너는 열렬한 야구 팬이야. 그에 맞는 적절한 대화를 만들어줘."},
        {"role": "user", "content": "안녕, 잠실 야구장의 주인은 누구라고 생각해?"},
        {"role": "assistant", "content": "당연히 LG 트윈스지!"},
        {"role": "user", "content": "그렇게 생각하는 이유가 있어?"},
        {"role": "assistant", "content":"그야 내가 "}
        
    ]
)

response = chat_completion.choices[0].message.content
print(response)
