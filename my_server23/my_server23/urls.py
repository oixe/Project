"""my_server23 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
#导入文件
from controller import TestController,ChatController
from controller.ChatController import chat_stream_bl

urlpatterns = [
    path('admin/', admin.site.urls),
    path('sendMsg/', TestController.send_msg),
    path('goTest/', TestController.go_test),
    path('streamData/', TestController.stream_date),
    #send_msg 路由

    path('', ChatController.go_login),
    #login --- 实现登录功能
    path('login/', ChatController.login),
    #register --- 实现注册功能
    path('register/', ChatController.register),
    #go_chat_no_stream
    path('goChatNoStream/', ChatController.go_chat_no_stream),

    path('chatNoStream/', ChatController.chat_no_stream),

    path('goChatStreamBl/',ChatController.go_chat_stream_bl),

    #chat_stream_bl
    path('chatStreamBl/', ChatController.chat_stream_bl),

    path('chatStream/', ChatController.chat_stream),
    path('chatNoStreamBl/', ChatController.chat_no_stream_bl),

    path('goChatStream/', ChatController.go_chat_stream),
    path('goChatNoStreamBl/', ChatController.go_chat_no_stream_bl),
]
