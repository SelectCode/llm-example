from langchain import PromptTemplate, OpenAI, LLMChain
import chainlit as cl
from langchain.chains import APIChain
from langchain.chains.api import open_meteo_docs
from langchain.chat_models import ChatOpenAI

template = """Question: {question}

Answer: Let's think step by step."""


@cl.on_chat_start
def main():
    llm = ChatOpenAI()
    api_chain = APIChain.from_llm_and_api_docs(llm, open_meteo_docs.OPEN_METEO_DOCS, verbose=True)

    # Store the chain in the user session
    cl.user_session.set("api_chain", api_chain)


@cl.on_message
async def main(question: str):
    prompt = PromptTemplate(template=template, input_variables=["question"])
    llm_chain = cl.user_session.get("llm_chain")  # type: APIChain
    res = llm_chain.run(prompt.format_prompt(question=question), callbacks=[cl.AsyncLangchainCallbackHandler()])
    await cl.Message(content=res).send()
