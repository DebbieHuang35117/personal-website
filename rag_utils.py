from langchain_huggingface import HuggingFaceEmbeddings


embedding_models: dict = {
    "e5": HuggingFaceEmbeddings(model_name="intfloat/multilingual-e5-large"),
}

default_embedding_model = embedding_models["e5"]
