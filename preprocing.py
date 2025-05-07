import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()  # Load variables from .env

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=GOOGLE_API_KEY) 
model = genai.GenerativeModel('gemini-pro')
def get(news):   
    response = model.generate_content(["your expert in summerizaing the steance in 1 or 2 lines but make sure that reading that you lines we should unberstnad whole sentace     sentace:"+news], stream=True) 
    response.resolve()   
    return response.text