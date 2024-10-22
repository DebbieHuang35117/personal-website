import os
from langchain.document_loaders.pdf import (
    PyPDFDirectoryLoader,
)  # Importing PDF loader from Langchain
from langchain.text_splitter import (
    RecursiveCharacterTextSplitter,
)  # Importing text splitter from Langchain
import shutil  # Importing shutil module for high-level file operations
from langchain.schema import Document
from rag_utils import default_embedding_model
from langchain.vectorstores.chroma import Chroma


DATA_PATH = os.path.join(os.path.dirname(__file__), "docs", "med-data")


def load_documents():
    """
    Load PDF documents from the specified directory using PyPDFDirectoryLoader.
    Returns:
    List of Document objects: Loaded PDF documents represented as Langchain
                                                            Document objects.
    """
    # Initialize PDF loader with specified directory
    document_loader = PyPDFDirectoryLoader(DATA_PATH)
    # Load PDF documents and return them as a list of Document objects
    return document_loader.load()


def split_text(documents: list[Document]):
    """
    Split the text content of the given list of Document objects into smaller chunks.
    Args:
      documents (list[Document]): List of Document objects containing text content to split.
    Returns:
      list[Document]: List of Document objects representing the split text chunks.
    """
    # Initialize text splitter with specified parameters
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=300,  # Size of each chunk in characters
        chunk_overlap=100,  # Overlap between consecutive chunks
        length_function=len,  # Function to compute the length of the text
        add_start_index=True,  # Flag to add start index to each chunk
    )

    # Split documents into smaller chunks using text splitter
    chunks = text_splitter.split_documents(documents)

    return chunks  # Return the list of split text chunks


CHROMA_PATH = os.path.join(os.path.dirname(__file__), "chroma_db")


def save_to_chroma(chunks: list[Document]):
    """
    Save the given list of Document objects to a Chroma database.
    Args:
    chunks (list[Document]): List of Document objects representing text chunks to save.
    Returns:
    None
    """

    # Clear out the existing database directory if it exists
    if os.path.exists(CHROMA_PATH):
        shutil.rmtree(CHROMA_PATH)

    # Create a new Chroma database from the documents using OpenAI embeddings
    db = Chroma.from_documents(
        chunks, default_embedding_model, persist_directory=CHROMA_PATH
    )

    # Persist the database to disk
    db.persist()
    print(f"Saved {len(chunks)} chunks to {CHROMA_PATH}.")


if __name__ == "__main__":
    print("Preparing database...")
    documents = load_documents()
    print(f"Loaded {len(documents)} documents.")
    chunks = split_text(documents)
    print(f"Split {len(chunks)} chunks.")
    save_to_chroma(chunks)
    print("Saved to Chroma database.")
