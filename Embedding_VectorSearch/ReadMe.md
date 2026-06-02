# FAISS Semantic Search Engine

## Overview

This project demonstrates a simple semantic search engine using:

- Sentence Transformers for text embeddings
- FAISS for vector similarity search
- Python CLI for interactive querying

The system converts knowledge base sentences into vector embeddings, stores them in a FAISS index, and retrieves the most semantically similar documents for a user query.

---

## Features

- Generate embeddings using all-MiniLM-L6-v2
- Store vectors in a FAISS index
- Perform Top-K semantic search
- Interactive command-line interface
- Cosine similarity using vector normalization

---

## Project Structure

```
FAISS_Semantic_Search/
│
├── semantic_search.py
├── theory_answers.md
├── requirements.txt
└── README.md
```

---

## Installation

### Create Virtual Environment

```bash
python -m venv venv
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Running the Project

```bash
python semantic_search.py
```

---

## Sample Knowledge Base

The project contains example support-related documents:

- Password reset
- Billing invoices
- Login issues
- Account settings
- Subscription upgrades
- Refund requests
- Payment methods
- Security settings

---

## Example Query

```
Enter query: How do I reset my password?
```

### Sample Output

```
Rank  Score    Matched Sentence

1     0.12     You can reset your password using the Forgot Password option.
2     0.34     If you cannot log in, check your username and password.
3     0.56     Two-factor authentication improves account security.
```

---

## Technologies Used

- Python
- Sentence Transformers
- FAISS
- NumPy

---

## Theory Topics Covered

- Vector Embeddings
- Semantic Search
- Cosine Similarity
- FAISS Indexing
- Approximate Nearest Neighbour (ANN)
- Retrieval-Augmented Generation (RAG)

---

## Author

Rohit Johnson
