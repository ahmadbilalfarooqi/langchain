from langchain_core.messages import HumanMessage, SystemMessage
from langchain_openai import OpenAI, ChatOpenAI
from decouple import config
SECRET_KEY = config('OPENAI_API_KEY')
# print(SECRET_KEY)

# Example 1 LLM's

# llm = OpenAI(api_key=SECRET_KEY)
# response = llm.invoke('who is the president of the United States?', )
# print(response)

# chatmodel
# example 1
# chat = ChatOpenAI(api_key=SECRET_KEY)
# respnse = chat.invoke('who is the president of the United States?')
# print(respnse.content)

# example 2
chat = ChatOpenAI(api_key=SECRET_KEY)
messages = [HumanMessage('Who is the prime minister of India?'),
            SystemMessage('You are a standup comedian.')]
respnse = chat.invoke(messages)
print(respnse.content)
