from openai import OpenAI
client = OpenAI(
    api_key= "your-key"
)

chat_completion = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        # {"role": "system", "content": "초등학교 5학년 학생을 대상으로 해서 가상의 영어 문답을 생성하려고 해."},
        {"role": "system", "content": "GRE를 대비하고 있는 수험생을 대상으로 해서 가상의 영어 문답을 생성하려고 해. 따라서 흔히 사용되지 않는 어려운 단어들로 답변해줘."},
        {"role": "user", "content": "Hello, ChatGPT! Can you introduce yourself?"}
        
    ]
)

response = chat_completion.choices[0].message.content
print(response)
