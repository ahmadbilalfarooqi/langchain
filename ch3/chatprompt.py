from langchain_core.prompts import ChatPromptTemplate, SystemMessagePromptTemplate, HumanMessagePromptTemplate, PromptTemplate
from langchain_openai import ChatOpenAI
from decouple import config
SECRET_KEY = config('OPENAI_API_KEY')

chat = ChatOpenAI(api_key=SECRET_KEY)



#================================================================================================
# # chat Model - Prompt Template
# # example 1 = message prompt Template as Tuples
# chatPrompot = ChatPromptTemplate.from_messages([
#     ("system",
#      "You are a helpful assistant that translates {input_language} to {output_language}."),
#     ("human", "{text}"),

# ])

# # print("Chat Prompt", chatPrompot)
# # print("chat prompt Input variables:", chatPrompot.input_variables)

# formattedChatPrompt = chatPrompot.format(input_language="English",
#                                          output_language="Spanish",
#                                          text="Hello, how are you?")

# # print("Formatted Chat Prompt", formattedChatPrompt)

# response = chat.invoke(formattedChatPrompt)
# # print("OpenAI Response: ",response)
# print("OpenAI Response of Content: ", response.content)





#================================================================================================
# Example 2 - Using Message Classes
# sys_template = "You are a helpful assistant that translates {input_language} to {output_language}."
# human_template = "{text}"
# chatPrompt = ChatPromptTemplate.from_messages([
#     SystemMessagePromptTemplate.from_template(sys_template),
#     HumanMessagePromptTemplate.from_template(human_template)
# ])

# # print("Chat Prompt", chatPrompt)

# formattedChatPrompt = chatPrompt.format(input_language="English",
#                                         output_language="Spanish",
#                                         text="Hello, how are you?")

# # print("Formatted Chat Prompt", formattedChatPrompt)

# response = chat.invoke(formattedChatPrompt)
# # print("OpenAI Response: ",response)
# print("OpenAI Response of Content: ", response.content)





#================================================================================================
# Example 3 - Using Prompt Template
# systemPrompt = PromptTemplate(input_variables=["input_language", "output_language"],
#                               template="You are a helpful assistant that translates {input_language} to {output_language}.")
# # systemPrompt  = PromptTemplate.from_template("You are a helpful assistant that translates {input_language} to {output_language}.")
# humanPrompt = PromptTemplate.from_template("{text}")
# systemMessagePrompt = SystemMessagePromptTemplate(prompt = systemPrompt)
# humanMessagePrompt  = HumanMessagePromptTemplate(prompt=humanPrompt)


# chatPrompt = ChatPromptTemplate.from_messages([systemMessagePrompt, humanMessagePrompt])

# # print("Chat Prompt", chatPrompt)

# formattedChatPrompt = chatPrompt.format_messages(
#             input_language = "English",
#             output_language = "French",
#             text = "I Love Programming"
# )

# print("Formatted Chat Prompt :", formattedChatPrompt)

# response  = chat.invoke(formattedChatPrompt)
# # print("OpenAI Response:", response)
# print("OpenAI content Response:", response.content)