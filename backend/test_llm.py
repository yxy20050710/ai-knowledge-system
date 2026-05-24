import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

print("API Key:", os.getenv("OPENAI_API_KEY"))
print("Base URL:", os.getenv("OPENAI_BASE_URL"))
print("Model:", os.getenv("OPENAI_MODEL"))

try:
    client = OpenAI(
        api_key=os.getenv("OPENAI_API_KEY"),
        base_url=os.getenv("OPENAI_BASE_URL"),
    )
    
    response = client.chat.completions.create(
        model=os.getenv("OPENAI_MODEL"),
        messages=[
            {"role": "user", "content": "Hello"}
        ]
    )
    print("Response:", response.choices[0].message.content)
except Exception as e:
    print("Error:", type(e).__name__, str(e))
