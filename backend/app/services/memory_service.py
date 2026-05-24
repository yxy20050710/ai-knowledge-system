chat_memory = {}

def get_chat_history(session_id):
    if session_id not in chat_memory: #不同id不同历史
        chat_memory[session_id] = []

    return chat_memory[session_id]

def add_message(session_id,role,content): # 添加消息到历史记录
    history = get_chat_history(session_id)

    history.append({
        "role":role,
        "content":content
    })