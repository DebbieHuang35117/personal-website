import os
import asyncio
import streamlit as st
from langchain_pinecone import PineconeVectorStore, PineconeEmbeddings
from langchain_openai import ChatOpenAI
from langchain.chains.question_answering import load_qa_chain
from langchain_openai import OpenAIEmbeddings

from dotenv import load_dotenv

load_dotenv()

llm = ChatOpenAI(
    model="gpt-4o",
    temperature=0,
    max_tokens=200,
    timeout=None,
    max_retries=2,
)

async def get_answer_multilingual_e5(query: str) -> str:
    embeddings = PineconeEmbeddings(model="multilingual-e5-large")
    index_name = "sinica-rag-test-0730-multilingual-e5-large"
    vectorstore = PineconeVectorStore(index_name=index_name, embedding=embeddings)
    docs = await asyncio.to_thread(vectorstore.similarity_search, query=query, k=1)
    chain = load_qa_chain(llm, chain_type="map_reduce")
    answer = await asyncio.to_thread(chain.run, input_documents=docs, question=query)
    return answer

async def get_answer_text_embedding_3_large(query: str) -> str:
    embeddings = OpenAIEmbeddings(model="text-embedding-3-large")
    index_name = "sinica-rag-test-0730-text-embedding-3-large"
    vectorstore = PineconeVectorStore(index_name=index_name, embedding=embeddings)
    docs = await asyncio.to_thread(vectorstore.similarity_search, query=query, k=1)
    chain = load_qa_chain(llm, chain_type="map_reduce")
    answer = await asyncio.to_thread(chain.run, input_documents=docs, question=query)
    return answer

async def get_answer_text_embedding_3_small(query: str) -> str:
    embeddings = OpenAIEmbeddings(model="text-embedding-3-small")
    index_name = "sinica-rag-test-0730-text-embedding-3-small"
    vectorstore = PineconeVectorStore(index_name=index_name, embedding=embeddings)
    docs = await asyncio.to_thread(vectorstore.similarity_search, query=query, k=1)
    chain = load_qa_chain(llm, chain_type="map_reduce")
    answer = await asyncio.to_thread(chain.run, input_documents=docs, question=query)
    return answer

async def get_answer_without_rag(query: str) -> str:
    chain = load_qa_chain(llm)
    answer = await asyncio.to_thread(chain.run, input_documents=[], question=query)
    return answer

async def main(query: str):
    answer_multilingual_e5 = await get_answer_multilingual_e5(query)
    answer_text_embedding_3_large = await get_answer_text_embedding_3_large(query)
    answer_text_embedding_3_small = await get_answer_text_embedding_3_small(query)
    answer_without_rag = await get_answer_without_rag(query)
    
    st.write(f'Answer (multilingual-e5-large): {answer_multilingual_e5}')
    st.write(f'Answer (text-embedding-3-large): {answer_text_embedding_3_large}')
    st.write(f'Answer (text-embedding-3-small): {answer_text_embedding_3_small}')
    st.write(f'Answer (without RAG): {answer_without_rag}')

st.title('2024-sinica-medLLM-rag-prototype-chat')
query = st.text_input('Enter your query:')

if st.button('Get Answer'):
    asyncio.run(main(query))
