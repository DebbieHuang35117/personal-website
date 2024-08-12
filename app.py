import os
import asyncio
import streamlit as st
from langchain_pinecone import PineconeVectorStore, PineconeEmbeddings
from langchain_openai import ChatOpenAI
from langchain.chains.question_answering import load_qa_chain
from langchain_openai import OpenAIEmbeddings
from langchain_huggingface import HuggingFacePipeline

from local_hf import READER_LLM


from dotenv import load_dotenv

load_dotenv()

llm = ChatOpenAI(
    model="gpt-4o-mini",
    temperature=0,
    max_tokens=200,
    timeout=None,
    max_retries=2,
)

hf_llm = HuggingFacePipeline(pipeline=READER_LLM)


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


async def main(query: str):
    answer_multilingual_e5 = await get_answer_multilingual_e5(query)
    answer_text_embedding_3_large = await get_answer_text_embedding_3_large(query)
    answer_text_embedding_3_small = await get_answer_text_embedding_3_small(query)
    answer_without_rag = await get_answer_without_rag(query)

    st.write(f'Answer (multilingual-e5-large): {answer_multilingual_e5}')
    st.write(
        f'Answer (text-embedding-3-large): {answer_text_embedding_3_large}')
    st.write(
        f'Answer (text-embedding-3-small): {answer_text_embedding_3_small}')
    st.write(f'Answer (without RAG): {answer_without_rag}')

    feedback_multilingual_e5 = st.radio(
        'Rate the answer (multilingual-e5-large)',
        options=[i for i in range(11)],  # 0 to 10
        index=5
    )
    feedback_text_embedding_3_large = st.radio(
        'Rate the answer (text-embedding-3-large)',
        options=[i for i in range(11)],  # 0 to 10
        index=5
    )
    feedback_text_embedding_3_small = st.radio(
        'Rate the answer (text-embedding-3-small)',
        options=[i for i in range(11)],  # 0 to 10
        index=5
    )
    feedback_without_rag = st.radio(
        'Rate the answer (without RAG)',
        options=[i for i in range(11)],  # 0 to 10
        index=5
    )

    if st.button('Submit Feedback'):
        st.write(
            f'Feedback (multilingual-e5-large): {feedback_multilingual_e5}')
        st.write(
            f'Feedback (text-embedding-3-large): {feedback_text_embedding_3_large}')
        st.write(
            f'Feedback (text-embedding-3-small): {feedback_text_embedding_3_small}')
        st.write(f'Feedback (without RAG): {feedback_without_rag}')

    # create a file to store the feedback
    with open('feedback.txt', 'a') as f:
        f.write(
            f'Query: {query}\nAnswer (multilingual-e5-large): {answer_multilingual_e5}\nFeedback (multilingual-e5-large): {feedback_multilingual_e5}\n\n')
        f.write(
            f'Query: {query}\nAnswer (text-embedding-3-large): {answer_text_embedding_3_large}\nFeedback (text-embedding-3-large): {feedback_text_embedding_3_large}\n\n')
        f.write(
            f'Query: {query}\nAnswer (text-embedding-3-small): {answer_text_embedding_3_small}\nFeedback (text-embedding-3-small): {feedback_text_embedding_3_small}\n\n')
        f.write(
            f'Query: {query}\nAnswer (without RAG): {answer_without_rag}\nFeedback (without RAG): {feedback_without_rag}\n\n')

st.title('2024-sinica-medLLM-rag-prototype-chat')
query = st.text_input('Enter your query:')

if st.button('Get Answer'):
    asyncio.run(main(query))
