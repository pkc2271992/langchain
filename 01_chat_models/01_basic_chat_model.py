import os
from dotenv import load_dotenv, dotenv_values
from langchain_openai import ChatOpenAI

load_dotenv()

API_KEY = os.getenv("apikey")

# Create a ChatOpenAI model
model = ChatOpenAI(model="gpt-4o",api_key=API_KEY)

# Invoke the model with a message
result = model.invoke("What is 81 divided by 9?")
print("Full result:")
print(result)
print("Content only:")
print(result.content)