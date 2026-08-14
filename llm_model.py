from dotenv import load_dotenv
import os
from langchain_openai import ChatOpenAI

load_dotenv()

llm = ChatOpenAI(
api_key=os.getenv("openrouter_API_KEY"),
base_url=os.getenv("openrouter_API_URL"),
model = 'openrouter/free',
temperature=0.8
)

# python llm_model.py