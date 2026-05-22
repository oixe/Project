# 引入需要的库
from idlelib.rpc import response_queue

import requests


def ollama_chat_no_stream(input):
    prompt = {
        "model": "deepseek-r1:1.5b",
        # system:系统 user：用户输入
        # content：内容
        "messages": [{"role": "system", "content": "你是一个专业的助手，请回答相关问题"},
                     {"role": "user", "content": input},
                     ],
        "stream": False
    }

    response = requests.post("http://localhost:11434/api/chat/", json=prompt)
    # 获取输出
    output = response.json()
    content = output.get("message").get("content")
    index = content.find("</think>")
    content = content[index + 8:-1]
    # 返回结果
    return content

