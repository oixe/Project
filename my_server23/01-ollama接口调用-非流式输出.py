# 引入需要的库
from idlelib.rpc import response_queue

import requests


#input函数，返回一个键盘输入的值
#构造函数
input = input("请输出问题：\n")
promot = {
    "model":"deepseek-r1:1.5b",
    #system:系统 user：用户输入
    #content：内容
    "messages": [{"role":"system","content":"你是一个专业的助手，请回答相关问题"},
                 {"role":"user","content":input},
                 ],
    "stream":False
}

response = requests.post("http://localhost:11434/api/chat/", json=promot)

#获取状态码
status_code = response.status_code
print("状态码：",status_code)
#h获取输出
output = response.json()
print("输出：",output)
content = output.get("message").get("content")
print("最终输出",content)
#查询content字符串第一个</think>标签的位置
index = content.find("</think>")
content = content[index+ 8:-1]
print("content:",content)