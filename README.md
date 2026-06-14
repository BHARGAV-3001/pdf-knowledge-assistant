# 📄 PDF Knowledge Assistant

A Retrieval-Augmented Generation (RAG) application that enables users to upload PDF documents and ask questions using natural language. The system performs semantic search over document content using vector embeddings and generates context-aware answers using Google's Gemini model.

---

## 🚀 Features

* Upload PDF documents
* Automatic text extraction
* Intelligent document chunking
* Semantic search using vector embeddings
* ChromaDB vector database integration
* Context-aware question answering
* Gemini-powered response generation
* Streamlit-based interactive UI
* MMR (Maximum Marginal Relevance) retrieval

---

## 🏗️ System Architecture

```text
User
 │
 ▼
Streamlit UI
 │
 ▼
PDF Upload
 │
 ▼
PyPDFLoader
 │
 ▼
Text Chunking
 │
 ▼
MiniLM Embeddings
 │
 ▼
ChromaDB Vector Store
 │
 ▼
MMR Retriever
 │
 ▼
Gemini LLM
 │
 ▼
Generated Answer
```

---

## 🧠 How It Works

### 1. Document Ingestion

The uploaded PDF is processed using PyPDFLoader to extract textual content.

### 2. Chunking

The extracted text is split into smaller overlapping chunks using RecursiveCharacterTextSplitter.

```python
chunk_size = 1000
chunk_overlap = 200
```

This preserves context while keeping chunks manageable for embedding generation.

### 3. Embedding Generation

Each chunk is converted into a dense vector representation using:

```text
sentence-transformers/all-MiniLM-L6-v2
```

Embeddings capture semantic meaning rather than simple keyword matching.

### 4. Vector Storage

Embeddings are stored inside ChromaDB for efficient similarity search.

### 5. Retrieval

When a user submits a query:

* The query is embedded
* Similar chunks are retrieved
* MMR retrieval selects diverse and relevant chunks

### 6. Answer Generation

Retrieved chunks are passed to Gemini along with the user's question.

Gemini generates an answer grounded in the retrieved document context.

---

## 🛠️ Tech Stack

### Frontend

* Streamlit

### Backend

* Python

### LLM

* Gemini 2.5 Flash

### RAG Framework

* LangChain

### Embeddings

* HuggingFace Sentence Transformers
* all-MiniLM-L6-v2

### Vector Database

* ChromaDB

### PDF Processing

* PyPDF

---

## 📂 Project Structure

```text
pdf-knowledge-assistant/
│
├── app.py
│
├── src/
│   ├── pdf_loader.py
│   ├── chunking.py
│   ├── embeddings.py
│   ├── vector_store.py
│   └── qa_engine.py
│
├── chroma_db/
│
├── .env.example
├── .gitignore
├── requirements.txt
└── README.md
```

---

## ⚙️ Installation

### Clone Repository

```bash
git clone https://github.com/yourusername/pdf-knowledge-assistant.git

cd pdf-knowledge-assistant
```

### Create Virtual Environment

```bash
python -m venv venv
```

Windows:

```bash
venv\Scripts\activate
```

Linux/Mac:

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Create Environment Variables

Create a `.env` file:

```env
GOOGLE_API_KEY=YOUR_GEMINI_API_KEY
```

---

## ▶️ Running the Application

```bash
streamlit run app.py
```

Open:

```text
http://localhost:8501
```

---

## 💬 Example Questions

```text
What projects are mentioned in the document?

Summarize the PDF.

What technologies were used?

List all technical skills.

Explain the architecture described in the document.
```

---

## 📊 Retrieval Strategy

The application uses:

```text
Maximum Marginal Relevance (MMR)
```

instead of standard similarity search.

Benefits:

* Reduces duplicate retrievals
* Improves context diversity
* Produces more relevant answers

---

## 🔍 Challenges Faced

### PDF Extraction Noise

Certain PDFs contain formatting artifacts that affect retrieval quality.

### Chunk Optimization

Experimented with:

* Chunk Size
* Chunk Overlap
* Retrieval Depth (K)

to improve answer relevance.

### Hallucination Reduction

Implemented context-grounded prompting to ensure answers are generated only from retrieved content.

---

## 📈 Future Improvements

* Multi-PDF Support
* OCR for scanned documents
* Citation-aware answers
* Conversational memory
* Hybrid search (BM25 + Vector Search)
* Re-ranking models
* FastAPI backend deployment
* Docker containerization
* User authentication

---

## 🎯 Key Concepts Demonstrated

* Retrieval-Augmented Generation (RAG)
* Semantic Search
* Vector Databases
* Embeddings
* Prompt Engineering
* Large Language Models
* LangChain
* Information Retrieval
* Document Intelligence


```
```
