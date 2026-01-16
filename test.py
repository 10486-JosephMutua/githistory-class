from langchain_groq import ChatGroq
from dotenv import load_dotenv
import os
load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")
llm = ChatGroq(llm="gpt-4o", api_key=GROQ_API_KEY)
llm.invoke("hi")