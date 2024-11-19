# custom code for the streamlit app
from taide_chat import taide_llm

# dependencies for streamlit and langchain
import streamlit as st
from streamlit_feedback import streamlit_feedback
from langchain_pinecone import PineconeVectorStore, PineconeEmbeddings
from langchain_openai import ChatOpenAI
from langchain.chains.question_answering import load_qa_chain
from langchain_openai import OpenAIEmbeddings
from langchain_huggingface import HuggingFacePipeline

# dependencies for system
import os
import asyncio
import os
import time
import datetime
import json
from dotenv import load_dotenv

load_dotenv()

SEARCH_TOP_K = int(os.getenv("SEARCH_TOP_K", 3))

# openai_llm = ChatOpenAI(model="gpt-4o-mini",temperature=0,max_tokens=200,timeout=None,max_retries=2)

# hf_llm = HuggingFacePipeline(pipeline=reader)

llm = taide_llm  # change this use different LLM provider

rag_pipelines = ["without-rag", "rag"]


def docs_to_dict(docs):
    return [
        {"page_content": doc.page_content, "metadata": doc.metadata} for doc in docs
    ]


async def get_answer_multilingual_e5(query: str) -> str:
    embeddings = PineconeEmbeddings(model="multilingual-e5-large")
    index_name = "sinica-rag-test-0730-multilingual-e5-large"
    vectorstore = PineconeVectorStore(index_name=index_name, embedding=embeddings)
    docs = await asyncio.to_thread(
        vectorstore.similarity_search, query=query, k=SEARCH_TOP_K
    )
    chain = load_qa_chain(llm, chain_type="map_reduce")
    answer = await asyncio.to_thread(chain.run, input_documents=docs, question=query)
    return answer, docs_to_dict(docs)


async def get_answer_text_embedding_3_large(query: str) -> str:
    embeddings = OpenAIEmbeddings(model="text-embedding-3-large")
    index_name = "sinica-rag-test-0730-text-embedding-3-large"
    vectorstore = PineconeVectorStore(index_name=index_name, embedding=embeddings)
    docs = await asyncio.to_thread(
        vectorstore.similarity_search, query=query, k=SEARCH_TOP_K
    )
    chain = load_qa_chain(llm, chain_type="map_reduce")
    answer = await asyncio.to_thread(chain.run, input_documents=docs, question=query)
    return answer, docs_to_dict(docs)


async def get_answer_text_embedding_3_small(query: str) -> str:
    embeddings = OpenAIEmbeddings(model="text-embedding-3-small")
    index_name = "sinica-rag-test-0730-text-embedding-3-small"
    vectorstore = PineconeVectorStore(index_name=index_name, embedding=embeddings)
    docs = await asyncio.to_thread(
        vectorstore.similarity_search, query=query, k=SEARCH_TOP_K
    )
    chain = load_qa_chain(llm, chain_type="map_reduce")
    answer = await asyncio.to_thread(chain.run, input_documents=docs, question=query)
    return answer, docs_to_dict(docs)


async def get_answer_without_rag(query: str) -> str:
    chain = load_qa_chain(llm)
    answer = await asyncio.to_thread(chain.run, input_documents=[], question=query)
    return answer, []


async def get_answer_chroma(query: str) -> str:
    from rag_utils import default_embedding_model
    from prepare_db import CHROMA_PATH
    from langchain_chroma import Chroma

    embeddings = default_embedding_model

    vectorstore = Chroma(persist_directory=CHROMA_PATH, embedding_function=embeddings)

    docs = await asyncio.to_thread(
        vectorstore.similarity_search, query=query, k=SEARCH_TOP_K
    )
    chain = load_qa_chain(llm, chain_type="map_reduce")
    answer = await asyncio.to_thread(chain.run, input_documents=docs, question=query)
    return answer, docs_to_dict(docs)


if "chat_history" not in st.session_state:
    st.session_state.chat_history = []


def display_answer():
    for i in st.session_state.chat_history:
        with st.chat_message("human"):
            st.write(i["question"])
        with st.chat_message("ai"):
            st.write(i["answers"])
        if "feedback" in i:
            with st.chat_message(avatar="👨‍💻", name="feedback"):
                st.write(i["feedback"])


async def create_answer(question):
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []

    # e5_answer, e5_docs = await get_answer_multilingual_e5(question)
    # text_embedding_3_large_answer, text_embedding_3_large_docs = (
    #    await get_answer_text_embedding_3_large(question)
    # )
    # text_embedding_3_small_answer, text_embedding_3_small_docs = (
    #    await get_answer_text_embedding_3_small(question)
    # )
    vanilla_answer, vanilla_docs = await get_answer_without_rag(question)
    chroma_answer, chroma_docs = await get_answer_chroma(question)

    st.session_state.chat_history.append(
        {
            "question": question,
            "answers": {
                "without-rag": vanilla_answer,
                "rag": chroma_answer,
            },
            "message_id": len(st.session_state.chat_history),
            "docs": {
                "without-rag": vanilla_docs,
                "rag": chroma_docs,
            },
        }
    )


def store_feedback(data):
    current_time = time.time()
    current_time_readable = datetime.datetime.fromtimestamp(current_time).strftime(
        "%Y-%m-%d_%H:%M:%S"
    )

    filepath = os.path.join(
        os.path.dirname(__file__), "logs", f"{current_time_readable}-log.json"
    )
    # if folder does not exist, create it
    if not os.path.exists(os.path.dirname(filepath)):
        os.makedirs(os.path.dirname(filepath))

    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)


def fbcb():
    message_id = len(st.session_state.chat_history) - 1
    if message_id >= 0:

        st.session_state.chat_history[message_id]["feedback"] = {}
        for pipeline in rag_pipelines:
            if f"fb_k_{pipeline}" in st.session_state:
                st.session_state.chat_history[message_id]["feedback"][pipeline] = (
                    st.session_state[f"fb_k_{pipeline}"]
                )
    display_answer()
    store_feedback(st.session_state.chat_history)


async def main():
    if question := st.chat_input(placeholder="Ask your question here .... !!!!"):
        await create_answer(question)
        display_answer()
        with st.form(f"feedback-form"):
            st.header("Feedback")

            for pipeline in rag_pipelines:
                st.write(pipeline)
                streamlit_feedback(
                    align="flex-start",
                    key=f"fb_k_{pipeline}",
                    feedback_type="faces",
                    optional_text_label="[Optional] Please provide an explanation",
                )
            st.form_submit_button("Save feedback", on_click=fbcb)


asyncio.run(main())
