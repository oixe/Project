#我们就可以把接口函数定义在这文件中

#接口一：客户端通过浏览器地址栏，发送一个请求访问接口函数，然后在网页中输出：{“msg”：“今天是周末”}
"""
    def:定义一个函数的关键字
    send_msg:函数的名字
    request:
        1、形参，这个函数就是客户端请求服务器接口的时候产生的，叫做请求对象
        2、这个对象内部就有很多的属性、函数等，用来获取客户端提交给服务器的内容，比如参数
    客户端需要{“msg”：“今天是周末“}数据，本质上就是让服务器返回一个json数据即可
    json数据可以和python中的字典相互转换，使用json包来实现
        1、json。loads（json数据） ---把json数据转为字典
        2、json。dumps（字典） --- 把字典转为json数据
    Django中如何把一个json数据返回给客户端【相应请求】呢？
        1、通过HttpResponse可以实现【课件中的方案】 --- 属于django提供的类
            1.1需要自己构建字典，然后转字典为json，再返回
        2、通过JsonResponse可以实现【本次项目中的方案】 --- 属于django提供的类
            2.1需要自己构建字典，直接返回，他会自动转换为json
"""
#导入JsonResponse
from django.http import JsonResponse,StreamingHttpResponse
#导入render
from django.shortcuts import render
#导入time
import time
#接口一：客户端通过浏览器地址栏，发送一个请求访问接口函数，然后在网页中输出：{“msg”：“今天是周末”}
def send_msg(request):
    return JsonResponse({
        'msg':'今天是周末'
    })

#接口二：访问test.html页面
def go_test(request):
   """
   django中访问页面通过render函数实现，步骤如下：
        1、导入render
        2、return render（参数一，参数二)
            2,1 参数一：request请求对象
            2.2 参数二：访问页面的路径，以templates为起点
   """
   return render(request=request,template_name="test.html")
def generate_data():
    for i in range(1,11):
        time.sleep(0.5)
        yield i
#接口三:流式输出
def stream_date(request):
    """
        django中如果想要实现流式输出，需要使用StreamingHttpResponse，参数2个
            1、参数一：一个迭代器对象
            2、参数二：返回数据以什么格式进行【这个格式都是一些固定的写法，不明白的格式直接网上查】
    """
    return StreamingHttpResponse(
        streaming_content=generate_data(),
        content_type="text/html;charset=utf-8"
    )
