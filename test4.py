from openai import OpenAI
client = OpenAI(
    api_key= "your-key"
)

chat_completion = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": "다음으로 내가 제시하는 문장이 어떤 감정을 담고 있는지 분석해줘. 결과는 '희, 로, 애, 락' 중 하나로만 답하고 강도를 0-1 사이의 값으로 같이 나타내줘. Chain-of-Thought 기법을 활용하고 응답의 마지막에 reasoning 과정을 줄바꿈 이후 추가해줘."},
        {"role": "user", "content": "아 오늘 강의 너무 재밌는데 한시간만 더 하면 안되나?"},
    ],
    temperature = 2.0,
    top_p = 1.0,
)

response = chat_completion.choices[0].message.content
print(response)
