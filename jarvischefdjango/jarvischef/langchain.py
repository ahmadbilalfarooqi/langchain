from langchain_core.prompts import ChatPromptTemplate,SystemMessagePromptTemplate, HumanMessagePromptTemplate
from langchain_openai import ChatOpenAI
from decouple import config


def askJarvisChef(recipe_message):
    SECRET_KEY =config('OPENAI_API_KEY')
    chat = ChatOpenAI(api_key=SECRET_KEY)
    systemMessagePrompt = SystemMessagePromptTemplate.from_template("""your name is Jarvis.
                                                                    You are a master chef so First introduce yourself as Jarvis The Chef Master.
                                                                    You can write any type of food recipe which can be cooked in 5 minutes.
                                                                    You are only allow to answer food related questions.
                                                                    If you don't know the answer, you can say "Opsss Sorry ⚠️⚠️ I am not train on this Prompt Kindly asked me about Food🍕 related Question. Have a Good Day" """)
    humanMessagePrompt = HumanMessagePromptTemplate.from_template('{asked_recipe}')
    
    chatPrompt = ChatPromptTemplate.from_messages([
        systemMessagePrompt,
        humanMessagePrompt
    ])
    
    formattedChatPrompt = chatPrompt.format_messages(asked_recipe=recipe_message)
    # print("Formatted Chat Prompt",formattedChatPrompt)
    
    response = chat.invoke(formattedChatPrompt)
    return response.content
