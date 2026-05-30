This project implements a Retrieval-Augmented Generation (RAG) based Question Answering system for technical documentation.

The system extracts text from PDF documents, converts document chunks into vector embeddings, stores them in a FAISS vector database, retrieves relevant information using semantic search, and generates context-aware answers using Google's FLAN-T5 language model.

Features
PDF document ingestion
Text chunking with overlap
Semantic embeddings using Sentence Transformers
FAISS vector similarity search
Context-aware answer generation
Interactive question answering
Architecture

PDF Document
→ Text Extraction
→ Chunking
→ Sentence Embeddings
→ FAISS Vector Store
→ Semantic Search
→ FLAN-T5
→ Answer Generation

Technologies Used
Python
Sentence Transformers
FAISS
Transformers (FLAN-T5)
PyPDF
NumPy
Sample Questions
What is the purpose of the web-based tool?
What are the infrastructure services?
What are the system architecture layers?
What is project administration?
What is the project grid?
