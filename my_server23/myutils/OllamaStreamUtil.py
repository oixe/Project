import os
from openai import OpenAI

def chat_stream(input):
    """
    使用 Ollama 的 OpenAI 兼容接口进行流式对话，并逐段返回响应内容。
    模型通过环境变量 OLLAMA_MODEL 指定，默认为 'deepseek-r1:1.5b'。
    """
    client = OpenAI(
        base_url="http://localhost:11434/v1",  # Ollama 的 OpenAI 兼容 API 地址
        api_key="ollama",                      # Ollama 不需要真实 API Key，但必须提供非空字符串
    )

    model = os.getenv("OLLAMA_MODEL", "deepseek-r1:1.5b")

    completion = client.chat.completions.create(
        model=model,
        messages=[
            {"role": "system", "content": "你是一个专业助手，请回答相关问题"},
            {"role": "user", "content": input},
        ],
        stream=True
    )

    for chunk in completion:
        content = chunk.choices[0].delta.content
        if content is not None:
            yield content