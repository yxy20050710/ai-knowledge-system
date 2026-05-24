import os

from openai import OpenAI
from dotenv import load_dotenv

load_dotenv() # 加载环境变量

client = OpenAI(
    api_key = os.getenv("OPENAI_API_KEY"),
    base_url = os.getenv("OPENAI_BASE_URL"),
) # 创建 OpenAI 客户端实例

SYSTEM_PROMPT = """
你是一名专业的企业ai助手。
你的特点：
- 你能够根据企业的需求，提供专业的建议和解决方案。
- 你能够与企业进行有效的沟通，理解企业的需求和问题。
- 回答结构化、尽量简洁
- 不要胡编乱造 不确定时直接说明
"""

def chat_with_ai(messages):
    response = client.chat.completions.create(
        model=os.getenv("OPENAI_MODEL"),
        messages=[
            {"role":"system","content":SYSTEM_PROMPT},
           
        ] + messages
    )
    return response.choices[0].message.content # 返回模型回复
