from langchain_community.vectorstores import Chroma


def create_vector_store(
    chunks,
    embeddings
):

    vectordb = Chroma.from_documents(
        documents=chunks,
        embedding=embeddings,
        persist_directory="chroma_db"
    )

    return vectordb


def retrieve_context(
    vectordb,
    question
):

    results = vectordb.max_marginal_relevance_search(
        question,
        k=5,
        fetch_k=20
    )

    return results