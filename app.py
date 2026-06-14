import os
import tempfile

import streamlit as st

from dotenv import load_dotenv

from src.pdf_loader import load_pdf
from src.chunking import create_chunks
from src.embeddings import get_embeddings
from src.vector_store import (
    create_vector_store,
    retrieve_context
)
from src.qa_engine import generate_answer

load_dotenv()

st.set_page_config(
    page_title="PDF Knowledge Assistant",
    page_icon="📄",
    layout="wide"
)

st.title("📄 PDF Knowledge Assistant")

st.markdown(
    """
Upload a PDF and ask questions about it.
"""
)

uploaded_file = st.file_uploader(
    "Upload PDF",
    type=["pdf"]
)

if uploaded_file:

    with tempfile.NamedTemporaryFile(
        delete=False,
        suffix=".pdf"
    ) as temp_file:

        temp_file.write(
            uploaded_file.read()
        )

        pdf_path = temp_file.name

    with st.spinner("Loading PDF..."):

        documents = load_pdf(pdf_path)

    with st.spinner("Creating chunks..."):

        chunks = create_chunks(
            documents
        )

    with st.spinner("Generating embeddings..."):

        embeddings = get_embeddings()

    with st.spinner("Creating vector database..."):

        vectordb = create_vector_store(
            chunks,
            embeddings
        )

    st.success(
        f"PDF processed successfully. "
        f"Created {len(chunks)} chunks."
    )

    question = st.text_input(
        "Ask a question about the PDF"
    )

    if question:

        with st.spinner("Searching document..."):

            retrieved_docs = retrieve_context(
                vectordb,
                question
            )

        context = "\n\n".join(
            [
                doc.page_content
                for doc in retrieved_docs
            ]
        )

        with st.spinner("Generating answer..."):

            answer = generate_answer(
                question,
                context
            )

        st.subheader("Answer")

        st.write(answer)

        with st.expander(
            "Retrieved Chunks"
        ):

            for i, doc in enumerate(
                retrieved_docs,
                start=1
            ):
                st.markdown(
                    f"### Chunk {i}"
                )
                st.write(
                    doc.page_content
                )