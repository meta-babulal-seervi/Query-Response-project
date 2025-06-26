from together import Together
import os 
from dotenv import load_dotenv

load_dotenv()  

api_Key = os.getenv("API_KEY")

def getResponse(user_input) :
    os.environ.get("TOGETHER_API_KEY")
    client = Together(api_key=api_Key) # auth defaults to os.environ.get("TOGETHER_API_KEY")
    response = client.chat.completions.create(
        model="meta-llama/Llama-4-Maverick-17B-128E-Instruct-FP8",
        messages=[
        {
            "role": "user",
            "content": f"{user_input}  please format your answer in Markdown."
        }
        ]
    )
    return response.choices[0].message.content

