from langchain.prompts import PromptTemplate
from langchain_openai import OpenAI
from decouple import config
SECRET_KEY = config('OPENAI_API_KEY')
# print(SECRET_KEY)
llm = OpenAI(api_key=SECRET_KEY,)
# print(llm)


#================================================================================================
# llm - prompts templates
# example 1 prompt having no input values

noInputPrompt = PromptTemplate(input_variables=[],
                               template="Tell me about the history of India in 10 words.")

# noInputPrompt = PromptTemplate.from_template(
#                                "Tell me about the history of the United States.")

formattednoInputPrompt = noInputPrompt.format()
# print(
#     f"noInputPrompt: {formattednoInputPrompt}\n\n"
# )

# now invoke the inputprompt to get the response from openai llm

response = llm.invoke(formattednoInputPrompt)
# print(response)


#================================================================================================
# # example 2 prompt having one input values

OneInputPrompt = PromptTemplate(input_variables=["country"],
                                template="Tell me about the history of the {country} in 50 words")

# OneInputPrompt = PromptTemplate.from_template(
#                                "Tell me about the history of the {country} in 10 words")

formattedOneInputPrompt = OneInputPrompt.format(country="United States")
# print(
#     f"OneInputPrompt: {formattedOneInputPrompt}\n\n"
# )

# now invoke the inputprompt to get the response from openai llm

response = llm.invoke(formattedOneInputPrompt)
# print(response)

#================================================================================================
# # example 3 prompt having multiple input values

multipleInputPrompt = PromptTemplate(input_variables=["country", "topic"],
                                template="Tell me about the history of the {country} {topic} in 50 words")

# OneInputPrompt = PromptTemplate.from_template(
#                                "Tell me about the history of the {country} {topic} in 10 words")

formattedmultipleInputPrompt = multipleInputPrompt.format(country="United States", topic="politics")
# print(
#     f"OneInputPrompt: {formattedOneInputPrompt}\n\n"
# )

# now invoke the inputprompt to get the response from openai llm

response = llm.invoke(formattedmultipleInputPrompt)
# print(response)


#================================================================================================
# # example 4 prompt having multiple no input values

template = "Tell me {language} {topic} trick"

promptTemplate = PromptTemplate.from_template(template)
# print("Prompt Template:", promptTemplate)
# print("Prompt Template input variable:", promptTemplate.input_variables)

formattedPromptTemplate = promptTemplate.format(language="python", topic="array")
# print("Formatted Prompt Template:", formattedPromptTemplate)


# now invoke the inputprompt to get the response from openai llm
response = llm.invoke(formattedPromptTemplate)
# print(response)
