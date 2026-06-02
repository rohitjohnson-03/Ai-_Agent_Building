# Conversational RAG Assistant

## Project Overview

This project implements a Conversational Retrieval-Augmented Generation (RAG) Assistant capable of:

* Maintaining conversation memory
* Understanding follow-up questions
* Rewriting contextual questions into standalone questions
* Retrieving relevant information from a PDF knowledge base using FAISS
* Calling external tools when required
* Routing between retrieval-based answering and tool-based answering

The system combines document retrieval with conversational context to provide more intelligent and accurate responses.

---

## Features

### 1. Conversation Memory

The assistant stores previous user interactions in a chat history list.

Example:

User: What is RAG?

User: Can you explain it more?

The assistant uses previous conversation history to understand that "it" refers to RAG.

---

### 2. History-Aware Retrieval

Before retrieval, follow-up questions are converted into standalone questions.

Example:

Input:
Can you explain it more?

Rewritten:
Can you explain RAG in more detail?

This improves retrieval quality and ensures accurate document search.

---

### 3. Vector Database

The knowledge base is created using:

* PyPDFLoader
* RecursiveCharacterTextSplitter
* HuggingFace Embeddings
* FAISS Vector Store

The PDF is split into chunks, converted into embeddings, and stored in FAISS for semantic search.

---

### 4. External Tool

Tool Implemented:

get_current_time()

Purpose:

Returns the current system date and time whenever requested by the user.

Example:

User: What is the current time?

Assistant: 2026-06-02 14:30:15

---

### 5. Routing Logic

The assistant decides whether to:

* Use document retrieval (RAG)
* Call an external tool

Current implementation:

* Questions containing "time" are routed to the tool.
* All other questions are routed through the retrieval pipeline.

---

## Project Structure

conversational-rag-assistant/

├── Conversational_RAG_Assistant.ipynb

├── tools.py

├── README.md

├── requirements.txt

└── screenshots/

    ├── retrieval_answer.png

    ├── followup_question.png

    └── tool_call.png

---

## How To Run

1. Install dependencies

pip install -r requirements.txt

2. Open Jupyter Notebook or Google Colab

3. Upload:

   * PDF document
   * tools.py

4. Run all notebook cells

5. Start chatting with the assistant

---

## Technologies Used

* Python
* LangChain
* FAISS
* HuggingFace Embeddings
* Sentence Transformers
* PyPDF
* Google Colab / Jupyter Notebook

---

## Screenshots

Include screenshots demonstrating:

1. Retrieval-based answer
2. Follow-up conversational question
3. Successful tool call

