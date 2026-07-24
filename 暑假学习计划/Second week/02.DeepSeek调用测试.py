import os
from openai import OpenAI

#创建AI大模型交互的客户端对象（DEEPSEEK_API_KEY环境变量的名字，值就是deepseek的api_key的）
client = OpenAI(api_key=os.environ.get('DEEPSEEK_API_KEY'),base_url="https://api.deepseek.com")

#与AI大模型进行交互
response = client.chat.completions.create(
    model="deepseek-v4-pro",
    messages=[
        {"role": "system", "content": "你是一名AI助理"},
        {"role": "user", "content": "你是谁"},
    ],
    stream=False,
    reasoning_effort="high",
    extra_body={"thinking": {"type": "enabled"}}
)

#输出大模型返回的结果
print(response.choices[0].message.content)