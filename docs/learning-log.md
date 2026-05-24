# AI Agent System Learning Log

---

# 2026-05-21

## 今日学习

### Git & GitHub

学习内容：

- git init
- git add
- git commit
- git push
- remote origin
- GitHub 仓库连接

问题：

- origin 拼写错误导致 push 失败
- 理解了本地仓库与远程仓库关系

收获：

- 初步理解 Git 工作流
- 理解团队协作基础
- 成功完成第一次代码提交

---

## 当前理解

AI 工程并不是传统全栈开发。

重点是：

- RAG
- Agent
- Workflow
- Tool Calling
- AI Pipeline
- 工程化部署

而不是单纯 CRUD。

---

## 当前目标

一周内完成：

企业级 AI Agent MVP

包括：

- RAG
- Agent
- Workflow
- Memory
- Docker 部署

# 2026-05-22

## 今日完成

- 初始化 Git 仓库
- 连接 GitHub
- 学习 push / commit
- 创建 backend
- 创建 Python 虚拟环境
- 安装 FastAPI
- 理解 requirements.txt
- 创建企业级项目结构
- 成功运行 FastAPI

  
## 遇到问题

1. 为什么要创建backend目录 为什么虚拟环境是在该目录下 是不是每次进入该项目都需要先进入虚拟环境 如何进入
   
## 学到什么

1. mkdir 在目录下创建文件
2. python -m venv venv 创建虚拟环境
3. 启动fastapi：uvicorn app.main:app --reload
4. cd .. 回到根目录
5. 代码推送步骤：
   - git add .
   - git commit -m "Initial commit"
   - git push
  
# 2026-05-23

什么是 RAG
什么是 Embedding
什么是 Chunk
为什么需要 Vector DB