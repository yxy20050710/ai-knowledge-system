from pypdf import PdfReader

def read_pdf(file_path:str):
    reader = PdfReader(file_path)
    text = ""
    for page in reader.pages: #读取所有页面
        text += page.extract_text() #提取文本
    return text