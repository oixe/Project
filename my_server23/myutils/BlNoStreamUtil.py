# 导入对应的包
import os
from openai import OpenAI


def chat_no_stream_bl(input):
    client = OpenAI(
        api_key=os.getenv("DASHSCOPE_API_KEY"),
        base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
    )
    completion = client.chat.completions.create(
        model="qwen3-max",
        messages=[
            {"role": "system", "content": "你是一个专业的助手，请根据用户问题进行回答"},
            {"role": "user", "content": input},
        ],
        stream=False
    )
    return completion.choices[0].message.content