from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings

embedding_model = HuggingFaceEmbeddings(
    model_name = "sentence-transformers/all-MiniLM-L6-v2",
)

vector_dbs = {} # 存放不同数据表的vector数据库

def get_vector_db(collection_name:str):

    if collection_name not in vector_dbs:
        vector_dbs[collection_name] = Chroma(
            collection_name = collection_name, #存放不同数据表
            embedding_function = embedding_model,
            persist_directory = "./chroma_db"
        )
    return vector_dbs[collection_name]

# 文本入库
def save_to_vector_db(
    collection_name,
    chunks,
    source
    ):
    metadata = [] #数据类型 存放数据来源
    for chunk in chunks:
        metadatas.append({
            "source":source
        }) #每个chunk都会记录来源
    # vector_db = get_vector_db(collection_name)
    vector_db.add_texts(chunks,metadatas=metadata)

    return "Text saved to vector database"


#检索
def search_docs(collection_name:str,query:str):
    vector_db = get_vector_db(collection_name)
    docs = vector_db.similarity_search(
        query,
        k = 3
    )
    return docs