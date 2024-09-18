from langchain.prompts import PromptTemplate
from langchain_openai import OpenAI
from decouple import config
SECRET_KEY = config('OPENAI_API_KEY')
# print(SECRET_KEY)
llm = OpenAI(api_key=SECRET_KEY,)
# print(llm)

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
