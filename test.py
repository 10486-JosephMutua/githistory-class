from langchain_groq import ChatGroq
GROQ_API_KEY = "gsk_lBMCdqaoYbmffCuBFY8MSEBm86dODWkWOvPuBDI4sX"
llm = ChatGroq(llm="gpt-4o", api_key=GROQ_API_KEY)
llm.invole("hi")