import os

from langchain_community.document_loaders import (
    TextLoader
)

from langchain_text_splitters import (
    RecursiveCharacterTextSplitter
)

from langchain_community.vectorstores import (
    FAISS
)

from langchain_community.embeddings import (
    HuggingFaceEmbeddings
)


def build_vector_store():

    docs = []

    folder = "knowledge_base"

    for file in os.listdir(folder):

        loader = TextLoader(
            os.path.join(folder, file)
        )

        docs.extend(
            loader.load()
        )

    splitter = (
        RecursiveCharacterTextSplitter(
            chunk_size=500,
            chunk_overlap=50
        )
    )

    chunks = splitter.split_documents(
        docs
    )

    embeddings = (
        HuggingFaceEmbeddings(
            model_name=
            "sentence-transformers/all-MiniLM-L6-v2"
        )
    )

    vector_store = FAISS.from_documents(
        chunks,
        embeddings
    )

    vector_store.save_local(
        "career_vector_db"
    )

    return vector_store