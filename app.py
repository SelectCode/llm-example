from langchain import PromptTemplate
from langchain.chains import APIChain
from langchain.chains.api import open_meteo_docs
from langchain.chat_models import ChatOpenAI

import chainlit as cl

template = """Input: {question}
Output: Let's think step by step."""


@cl.langchain_factory(use_async=True)
def factory():
    prompt = PromptTemplate(template=template, input_variables=["question"])
    llm = ChatOpenAI()
    llm_chain = APIChain.from_llm_and_api_docs(llm, open_meteo_docs.OPEN_METEO_DOCS, verbose=True)
    return llm_chain
