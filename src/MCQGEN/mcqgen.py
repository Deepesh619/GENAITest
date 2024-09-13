from langchain.prompts import PromptTemplate
from langchain_huggingface import HuggingFaceEndpoint
from langchain.chains import LLMChain
from dotenv import load_dotenv
import os
load_dotenv()
key = os.getenv("HUGGINGFACEHUB_API_TOKEN")
model_id= "microsoft/Phi-3-mini-4k-instruct"
llm= HuggingFaceEndpoint (
    repo_id=model_id
    #add_to_git_credential=True
)

prompt= PromptTemplate(
input_variables=["text"],
template= "{text}"
)
        
def test(text):
        chain = prompt | llm
        response = chain.invoke(text)
        return response
