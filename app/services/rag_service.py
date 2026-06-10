from langchain_community.vectorstores import (
    FAISS
)

from langchain_community.embeddings import (
    HuggingFaceEmbeddings
)


embeddings = (
    HuggingFaceEmbeddings(
        model_name=
        "sentence-transformers/all-MiniLM-L6-v2"
    )
)


def search_knowledge_base(
    query: str
):

    vector_store = FAISS.load_local(
        "career_vector_db",
        embeddings,
        allow_dangerous_deserialization=True
    )

    docs = (
        vector_store.similarity_search(
            query,
            k=3
        )
    )

    return docs