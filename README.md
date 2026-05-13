# Industrial-RAG-Assistant
This project implements an end-to-end Retrieval-Augmented Generation (RAG) system designed to query and interact with industrial technical documentation using Large Language Models (LLMs).

The system combines semantic search, vector databases, and LLM-based generation to provide accurate, context-aware answers over domain-specific documents.

# Key Features
- PDF document ingestion and text extraction
- Semantic chunking with overlap strategy
- Text embeddings using Transformer-based models
- Vector similarity search (semantic retrieval)
- Retrieval-Augmented Generation (RAG) pipeline
- LLM-based question answering over private documents
- Experiment tracking with MLflow (WIP / optional)
- REST API or interactive UI (FastAPI / Streamlit)

# Tech Stack
## Machine Learning & NLP
- Python
- PyTorch
- Hugging Face Transformers
- Sentence Transformers

## RAG & LLM Stack
- LangChain / LlamaIndex
- OpenAI / Mistral / Llama (depending on setup)

## Vector Search
- ChromaDB / FAISS

## MLOps & Deployment
- MLflow (experiment tracking)
- FastAPI / Streamlit (serving)

## Data Processing
- Pandas
- NumPy

# Project Goals
This project was built to:

- Explore modern NLP pipelines beyond classical ML
- Implement a full RAG architecture from scratch
- Gain experience with LLM orchestration and embeddings
- Introduce MLOps practices in experimental ML systems
- Simulate real-world AI assistant applications in industry
