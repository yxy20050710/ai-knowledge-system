# PDF文件
from fileinput import filename
import os
from fastapi import APIRouter,UploadFile,File # 上传文件的路由
from app.services.pdf_service import read_pdf
from app.services.chunk_service import split_text
from app.services.vector_service import save_to_vector_db

router = APIRouter()

UPLOAD_DIR = "uploads"

@router.post("/upload")

# async 异步
async def upload_pdf(
    collection_name:str,
    file:UploadFile = File(...)
    ):
    file_path = os.path.join(UPLOAD_DIR,file.filename)
    with open(file_path,"wb") as f:
        content = await file.read()
        f.write(content)

    text = read_pdf(file_path)

    chunks = split_text(text)

    save_to_vector_db(
        collection_name=collection_name,
        chunks=chunks,
        source=file.filename # 数据来源
        )

    return {
        "message":"PDF 文件上传成功",
        "chunks":len(chunks)
    }
