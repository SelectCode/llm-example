from langchain import PromptTemplate, LLMChain
from langchain.chains import RetrievalQA
from langchain.chat_models import ChatOpenAI

import chainlit as cl

from utils import get_docsearch

template = """Input: {question}
Output: Let's think step by step."""


@cl.langchain_factory(use_async=True)
async def factory():
    files = None
    while files is None:
        files = await cl.AskFileMessage(
            content="Select File",
            accept=["text/plain", "application/pdf"],
            max_size_mb=20,
            timeout=180,
        ).send()
    file = files[0]
    msg = cl.Message(content=f"Processing `{file.name}`...")
    await msg.send()
    docsearch = await cl.make_async(get_docsearch)(file)
    llm_chain = RetrievalQA.from_chain_type(
        ChatOpenAI(temperature=0, streaming=True),
        chain_type="stuff",
        retriever=docsearch.as_retriever(max_tokens_limit=4097),
    )
    await msg.update(content=f"`{file.name}` processed. You can now ask questions!")
    return llm_chain
