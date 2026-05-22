import json
from django.http import JsonResponse,StreamingHttpResponse
from django.shortcuts import render
import pymysql
from myutils import OllamaNoStreamUtil,BlStreamUtil,OllamaStreamUtil,BlNoStreamUtil
from myutils.OllamaNoStreamUtil import ollama_chat_no_stream
#接口一
def go_login(request):
    return render(request=request,template_name="login.html")
#接口二:实现登录功能
"""
        django中取出客户端传过来的json数据，步骤如下：
            1.json_Data = request.body---从请求体里面获取参数内容，返回值类型byte
            ---返回值类型byte满足键值对格式,可以直接用json.loads()转为字典
"""
def login(request):
        json_data = request.body
        dict_data=json.loads(json_data)
        #获取参数
        username = dict_data.get("username")
        password = dict_data.get("password")
        #1.获取数据库连接对象
        conn = pymysql.connect(
            host="127.0.0.1",
            port=3306,
            user="root",
            password="123456",
            database="sanxia23",
            charset="utf8",
        )
        #2通过连接对象获取游标对象
        cur = conn.cursor()
        #3定义操作的sql语句 %s是个占位符，表示username字段的值，后面执行sql的时候再把真实的值传给%S占位的地方
        sql = "select * from user where username = %s"
        #4通过游标对象执行sql语句，如果有参数，给参数赋值---execute(sql语句,如果有%s就在这里传值)
        cur.execute(sql,[username])
        #5获取查询的结果---fetchall获取查询到的所有数据
        query_data = cur.fetchall()
        #6关闭游标对象、连接对象
        cur.close()
        conn.close()
        #7基于查询结果的结果做逻辑处理

        #账号验证
        if not query_data:
            return JsonResponse({
                "code":500,
                "msg":"账号不存在"
            })
        #密码验证
        if password !=query_data[0][2]:
            return JsonResponse({
                "code":"500",
                "msg":"密码错误"
            })
        return JsonResponse({
            "code":200,
            "msg":"登陆成功"
        })

#接口九:实现注册功能
def register(request):
    json_data = request.body
    dict_data = json.loads(json_data)
    #获取参数
    username = dict_data.get("username")
    password = dict_data.get("password")
    
    # 验证参数
    if not username or not password:
        return JsonResponse({
            "code": 500,
            "msg": "用户名和密码不能为空"
        })
    
    #1.获取数据库连接对象
    conn = pymysql.connect(
        host="127.0.0.1",
        port=3306,
        user="root",
        password="123456",
        database="sanxia23",
        charset="utf8",
    )
    try:
        #2通过连接对象获取游标对象
        cur = conn.cursor()
        #3检查用户名是否已存在
        sql_check = "select * from user where username = %s"
        cur.execute(sql_check, [username])
        query_data = cur.fetchall()
        
        if query_data:
            # 用户名已存在
            cur.close()
            conn.close()
            return JsonResponse({
                "code": 500,
                "msg": "用户名已存在，请使用其他用户名"
            })
        
        #4插入新用户
        sql_insert = "insert into user (username, password) values (%s, %s)"
        cur.execute(sql_insert, [username, password])
        #5提交事务
        conn.commit()
        #6关闭游标对象、连接对象
        cur.close()
        conn.close()
        
        return JsonResponse({
            "code": 200,
            "msg": "注册成功，请登录"
        })
    except Exception as e:
        # 发生异常时回滚
        conn.rollback()
        cur.close()
        conn.close()
        return JsonResponse({
            "code": 500,
            "msg": f"注册失败：{str(e)}"
        })

#接口三 访问chat_no_stream.html9页面
def go_chat_no_stream(request):
    return render(request=request,template_name="chat_no_stream.html")

#接口四 非流式对话---ollama实现
def chat_no_stream(request):

    input = request.GET.get("message")
    #调用模型进行对话
    result = OllamaNoStreamUtil.ollama_chat_no_stream(input)

    return JsonResponse({
        "code": 200,
        "msg":"请求成功",
        "data":result
    })
#接口五 访问chat_stream_bl.html
def go_chat_stream_bl(request):
    return render(request=request,template_name="chat_stream_bl.html")
#接口六 百炼流式对话 ---百炼开放平台
def chat_stream_bl(request):
    message = request.GET.get("message")
    return StreamingHttpResponse(
        streaming_content=BlStreamUtil.chat_stream_bl(message),
        content_type="text/plain;charset=utf-8"
    )

#接口七 Ollama流式对话
def chat_stream(request):
    message = request.GET.get("message")
    return  StreamingHttpResponse(
        streaming_content=OllamaStreamUtil.chat_stream(message),
        content_type="text/plain;charset=utf-8"
    )

# 接口八 百炼平台非流式输出
def chat_no_stream_bl(request):
    input = request.GET.get("message")
    # 调用模型进行对话
    result = BlNoStreamUtil.chat_no_stream_bl(input)

    return JsonResponse({
        "code": 200,
        "msg": "请求成功",
        "data": result
    })

def go_chat_stream(request):
    return render(request=request, template_name="chat_stream.html")

def go_chat_no_stream_bl(request):
    return render(request=request, template_name="chat_no_stream_bl.html")
