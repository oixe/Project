# My Server 23 - 本地大模型对话平台

基于 Django 开发的本地大语言模型（LLM）对话 Web 应用，支持 Ollama 本地模型和阿里云百炼平台，提供流式和非流式两种响应模式。

## 功能特性

- **用户系统** — 注册、登录，基于 MySQL 存储用户信息
- **双后端支持** — 同时支持本地 Ollama 模型和阿里云百炼平台
- **流式/非流式响应** — 流式模式实时逐字输出，非流式模式等待完整回复
- **Markdown 渲染** — 对话内容支持 Markdown 格式，代码高亮显示
- **模型切换** — 前端下拉框可切换不同模型
- **复制/重新生成** — 支持复制回复内容和重新生成回答

## 技术栈

| 层级 | 技术 |
|------|------|
| 后端框架 | Django 3.2 |
| 数据库 | MySQL（用户存储）|
| LLM 后端 | Ollama（本地） / 阿里云百炼（云端）|
| API 客户端 | OpenAI SDK / requests |
| 前端框架 | Vue.js + Element UI |
| HTTP 客户端 | Axios |
| Markdown | marked.js + DOMPurify |

## 项目结构

```
my_server23/
├── my_server23/                    # Django 项目根目录
│   ├── manage.py                   # Django 入口
│   ├── my_server23/                # 项目配置
│   │   ├── settings.py             # Django 配置
│   │   ├── urls.py                 # 路由配置
│   │   └── ...
│   ├── controller/                 # 控制器层
│   │   ├── ChatController.py       # 登录/注册/聊天接口
│   │   └── TestController.py       # 测试接口
│   ├── myutils/                    # LLM 调用工具
│   │   ├── OllamaNoStreamUtil.py   # Ollama 非流式调用
│   │   ├── OllamaStreamUtil.py     # Ollama 流式调用
│   │   ├── BlNoStreamUtil.py       # 百炼非流式调用
│   │   └── BlStreamUtil.py         # 百炼流式调用
│   ├── templates/                  # 前端页面
│   │   ├── login.html              # 登录/注册页
│   │   ├── chat_no_stream.html     # Ollama 非流式聊天
│   │   ├── chat_stream.html        # Ollama 流式聊天
│   │   ├── chat_no_stream_bl.html  # 百炼非流式聊天
│   │   └── chat_stream_bl.html     # 百炼流式聊天
│   └── static/                     # 前端静态资源
│       ├── JS/vue.js
│       ├── axios/
│       ├── element-ui/
│       ├── marked/
│       └── dompurify/
```

## 环境要求

- Python 3.12+
- MySQL（本地运行于 `localhost:3306`）
- Ollama（本地运行于 `localhost:11434`，如需使用本地模型）
- 阿里云百炼 API Key（如需使用百炼平台）

## 安装与运行

### 1. 安装 Python 依赖

```bash
pip install django pymysql openai requests
```

### 2. 配置 MySQL 数据库

创建数据库和用户表：

```sql
CREATE DATABASE sanxia23;

USE sanxia23;

CREATE TABLE user (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(255) NOT NULL,
    password VARCHAR(255) NOT NULL
);
```

> 默认连接配置：`host=127.0.0.1`, `port=3306`, `user=root`, `password=123456`, `database=sanxia23`
> 如需修改，请编辑 `controller/ChatController.py` 中的数据库连接参数。

### 3. 配置环境变量

```bash
# 阿里云百炼 API Key（可选，使用百炼功能时需要）
export DASHSCOPE_API_KEY=your_api_key_here

# Ollama 模型名称（可选，默认 deepseek-r1:1.5b）
export OLLAMA_MODEL=deepseek-r1:1.5b
```

### 4. 安装 Ollama 本地模型（可选）

```bash
# 安装 Ollama 后，拉取模型
ollama pull deepseek-r1:1.5b
```

### 5. 启动服务

```bash
cd my_server23
python manage.py runserver
```

访问 http://localhost:8000/ 即可使用。

## API 接口

### 用户相关

| 接口 | 方法 | 说明 |
|------|------|------|
| `/` | GET | 登录/注册页面 |
| `/login/` | POST | 用户登录 |
| `/register/` | POST | 用户注册 |

### Ollama 聊天

| 接口 | 方法 | 说明 |
|------|------|------|
| `/goChatNoStream/` | GET | 非流式聊天页面 |
| `/chatNoStream/` | GET | 非流式聊天接口，参数 `?message=xxx` |
| `/goChatStream/` | GET | 流式聊天页面 |
| `/chatStream/` | GET | 流式聊天接口，参数 `?message=xxx` |

### 百炼平台聊天

| 接口 | 方法 | 说明 |
|------|------|------|
| `/goChatNoStreamBl/` | GET | 非流式聊天页面 |
| `/chatNoStreamBl/` | GET | 非流式聊天接口，参数 `?message=xxx` |
| `/goChatStreamBl/` | GET | 流式聊天页面 |
| `/chatStreamBl/` | GET | 流式聊天接口，参数 `?message=xxx` |

## 使用模式

登录后可在四种模式间切换：

| 模式 | 后端 | 响应方式 |
|------|------|----------|
| Ollama 非流式 | 本地 Ollama | 等待完整回复后一次性显示 |
| Ollama 流式 | 本地 Ollama | 逐字实时显示回复 |
| 百炼非流式 | 阿里云百炼 | 等待完整回复后一次性显示 |
| 百炼流式 | 阿里云百炼 | 逐字实时显示回复 |

## License

MIT
