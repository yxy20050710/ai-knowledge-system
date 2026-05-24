from app.services.vector_service import search_docs
from app.services.llm_service import client,chat_with_ai
from app.services.memory_service import(
    get_chat_history,
    add_message
)

def rag_chat(session_id:str,collection_name:str,question:str):
    history = get_chat_history(session_id)
    docs = search_docs(collection_name,question)
    context = "\n\n".join([
        doc.page_content for doc in docs
    ])

    prompt = f"""
    你是一个专业的知识问答机器人，你的任务是基于以下知识回答问题。
    知识内容：{context}
    用户问题：{question}
    根据历史聊天与知识库内容进行回答。
    """

    messages = history +[
        {
            "role":"user",
            "content":prompt
        }
    ] #拼接历史记录和当前问题--上下文记忆
    # response = client.chat.completions.create(
    #     model = os.getenv("OPENAI_MODEL"),
    #     messages = [
    #         {"role":"user","content":prompt}
    #     ]
    # ) 不用重复写 直接调用
    answer = chat_with_ai(messages)
    add_message(session_id,"user",question) # 添加用户问题到历史记录
    add_message(session_id,"assistant",answer) # 添加助手回答到历史记录

    return {
        "answer": answer,
        "sources": [doc.metadata["source"] for doc in docs]
    }

    """
    history存放历史记录
    message-拼接当前对话：历史记录+当前问题（question+prompt）
    当llm根据messages 结合 rag 给出回答ansewr之后
    调用add_message将用户问题question和模型回答answwer存入history当中 作为上下文记忆

    """