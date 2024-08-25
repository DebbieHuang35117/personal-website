# custom code for the streamlit app
from local_hf import reader

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

openai_llm = ChatOpenAI(
    model="gpt-4o-mini",
    temperature=0,
    max_tokens=200,
    timeout=None,
    max_retries=2,
)

hf_llm = HuggingFacePipeline(pipeline=reader)

llm = openai_llm


async def get_answer_multilingual_e5(query: str) -> str:
    embeddings = PineconeEmbeddings(model="multilingual-e5-large")
    index_name = "sinica-rag-test-0730-multilingual-e5-large"
    vectorstore = PineconeVectorStore(
        index_name=index_name, embedding=embeddings)
    docs = await asyncio.to_thread(vectorstore.similarity_search, query=query, k=1)
    chain = load_qa_chain(llm, chain_type="map_reduce")
    answer = await asyncio.to_thread(chain.run, input_documents=docs, question=query)
    return answer


async def get_answer_text_embedding_3_large(query: str) -> str:
    embeddings = OpenAIEmbeddings(model="text-embedding-3-large")
    index_name = "sinica-rag-test-0730-text-embedding-3-large"
    vectorstore = PineconeVectorStore(
        index_name=index_name, embedding=embeddings)
    docs = await asyncio.to_thread(vectorstore.similarity_search, query=query, k=1)
    chain = load_qa_chain(llm, chain_type="map_reduce")
    answer = await asyncio.to_thread(chain.run, input_documents=docs, question=query)
    return answer


async def get_answer_text_embedding_3_small(query: str) -> str:
    embeddings = OpenAIEmbeddings(model="text-embedding-3-small")
    index_name = "sinica-rag-test-0730-text-embedding-3-small"
    vectorstore = PineconeVectorStore(
        index_name=index_name, embedding=embeddings)
    docs = await asyncio.to_thread(vectorstore.similarity_search, query=query, k=1)
    chain = load_qa_chain(llm, chain_type="map_reduce")
    answer = await asyncio.to_thread(chain.run, input_documents=docs, question=query)
    return answer


async def get_answer_without_rag(query: str) -> str:
    chain = load_qa_chain(llm)
    answer = await asyncio.to_thread(chain.run, input_documents=[], question=query)
    return answer


if "chat_history" not in st.session_state:
    st.session_state.chat_history = []


def display_answer():
    for i in st.session_state.chat_history:
        with st.chat_message("human"):
            st.write(i["question"])
        with st.chat_message("ai"):
            st.caption(i["type"])
            st.write(i["answer"])

        # If there is no feedback show N/A
        if "feedback" in i:
            st.write(f"Feedback: {i['feedback']}")
        else:
            st.write("Feedback: N/A")


async def create_answer(question):
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []


    st.session_state.chat_history.append({
        "question": question,
        "answer": await get_answer_multilingual_e5(question),
        "message_id": len(st.session_state.chat_history),
        "type": "rag-multilingual_e5"
    })
    st.session_state.chat_history.append({
        "question": question,
        "answer": await get_answer_text_embedding_3_large(question),
        "message_id": len(st.session_state.chat_history),
        "type": "rag-text_embedding_3_large"
    })
    st.session_state.chat_history.append({
        "question": question,
        "answer": await get_answer_text_embedding_3_small(question),
        "message_id": len(st.session_state.chat_history),
        "type": "rag-text_embedding_3_small"
    })
    st.session_state.chat_history.append({
        "question": question,
        "answer": await get_answer_without_rag(question),
        "message_id": len(st.session_state.chat_history),
        "type": "vanilla"
    })


def store_feedback(data):
    current_time = time.time()
    current_time_readable = datetime.datetime.fromtimestamp(
        current_time).strftime('%Y-%m-%d_%H:%M:%S')

    filepath = os.path.join(os.path.dirname(__file__),
                            "logs", f"{current_time_readable}-log.json")
    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)


def fbcb(message_id):
    if message_id >= 0:
        st.session_state.chat_history[message_id][
            "feedback"] = st.session_state[f"fb_k_{message_id}"]
    display_answer()
    store_feedback(
        st.session_state.chat_history
    )


async def main():
    if question := st.chat_input(placeholder="Ask your question here .... !!!!"):
        await create_answer(question)
        display_answer()
        for i, _ in enumerate(st.session_state.chat_history):
            with st.form(f'feedback-form-{i}'):
                streamlit_feedback(feedback_type="thumbs",
                                   align="flex-start", key=f'fb_k_{i}')
                st.form_submit_button('Save feedback', on_click=fbcb(i))
asyncio.run(main())
