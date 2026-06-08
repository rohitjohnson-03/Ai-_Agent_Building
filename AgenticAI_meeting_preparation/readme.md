

## Overview

The Agentic AI Meeting Preparation Assistant helps users prepare for upcoming client meetings by automatically retrieving and analyzing information from multiple sources.

Instead of manually searching through client documents, meeting notes, and historical records, users can ask:

> "Prepare me for my meeting with Acme Corp."

The assistant retrieves relevant information, reasons over the data, and generates a concise meeting brief containing key discussion points, open action items, decision makers, and recommended next steps.

---

## Features

### Retrieval-Augmented Generation (RAG)

* Uses FAISS as a Vector Database.
* Stores client profiles, meeting notes, and memory documents as embeddings.
* Retrieves relevant information before generating responses.

### Agentic Workflow

The assistant follows a multi-step reasoning process:

1. Identify the client.
2. Retrieve client profile information.
3. Retrieve previous meeting notes.
4. Retrieve long-term memory.
5. Analyze retrieved context.
6. Generate a meeting preparation brief.

### Short-Term Memory

Maintains conversation history during the current session.

Example:

User:
Prepare me for my meeting with Acme Corp.

User:
What action items are still pending?

The assistant remembers previous context and provides follow-up responses.

### Long-Term Memory

Stores historical information about clients, including:

* Previous discussions
* Decision makers
* Open concerns
* Business priorities

### Tool Usage

The assistant uses three retrieval tools:

#### Tool 1: Client Information Retrieval

Retrieves company profile information.

#### Tool 2: Meeting Notes Retrieval

Retrieves previous meeting discussions and action items.

#### Tool 3: Long-Term Memory Retrieval

Retrieves historical client context and stored knowledge.

---

## Architecture

```text
                    User
                      │
                      ▼
        Agentic AI Meeting Assistant
                      │
      ┌───────────────┼───────────────┐
      ▼               ▼               ▼

Client Info     Meeting Notes     Long-Term Memory
 Retrieval       Retrieval         Retrieval

      ▼               ▼               ▼

              FAISS Vector Stores

                      │
                      ▼

            Meeting Brief Generator
                      │
                      ▼

              Final Meeting Brief
```

---

## Project Structure

```text
Agentic-AI-Meeting-Preparation-Assistant/

│
├── app.py
│
├── data/
│   ├── acme_profile.txt
│   ├── acme_meeting_notes.txt
│   └── client_memory.txt
│
├── screenshots/
│   ├── demo.png
│
├── requirements.txt
│
└── README.md
```

---

## Technologies Used

| Component       | Technology                |
| --------------- | ------------------------- |
| LLM             | Hugging Face Transformers |
| Vector Database | FAISS                     |
| Embeddings      | Sentence Transformers     |
| Framework       | LangChain                 |
| Memory          | Custom Memory Store       |
| Language        | Python                    |

---

## Installation

Install required packages:

```bash
pip install -r requirements.txt
```

Or in Google Colab:

```python
!pip install -q \
langchain==0.2.17 \
langchain-community==0.2.19 \
langchain-core==0.2.43 \
faiss-cpu \
sentence-transformers \
transformers
```

---

## Dataset

The project uses three sample documents:

### Client Profile

Contains:

* Company information
* Industry
* Products
* Challenges
* Opportunities

### Meeting Notes

Contains:

* Previous discussions
* Requests
* Open action items

### Long-Term Memory

Contains:

* Historical information
* Decision makers
* Business priorities
* Previous concerns

---

## Running the Application

Run:

```bash
python app.py
```

Example Prompt:

```text
Prepare me for my meeting with Acme Corp
```

---

## Example Output

```text
MEETING BRIEF

Client:
Acme Corp

Industry:
Manufacturing

Business Challenges:
- Production downtime
- Predictive maintenance requirements

Previous Discussions:
- Pricing proposal requested
- Deployment timeline discussed

Open Action Items:
- Send pricing proposal
- Share architecture diagram
- Schedule workshop

Decision Makers:
- John Smith (CTO)
- Emily Brown (Operations Head)

Talking Points:
- Predictive maintenance solution
- ROI analysis
- Deployment timeline

Recommended Next Actions:
- Present proposal
- Confirm workshop date
- Schedule technical discussion
```

---

## Assignment Requirements Mapping

| Requirement              | Implementation                    |
| ------------------------ | --------------------------------- |
| RAG                      | FAISS Vector Database             |
| Vector Search            | Similarity Search                 |
| Agentic Workflow         | Multi-step Retrieval + Generation |
| Short-Term Memory        | Conversation History              |
| Long-Term Memory         | Memory Documents                  |
| Tool Usage               | 3 Retrieval Tools                 |
| Meeting Brief Generation | LLM-based Summary                 |
| Multi-source Retrieval   | Client, Notes, Memory             |

---

## Future Improvements

* Support multiple clients
* Email integration
* Calendar integration
* CRM integration
* Real-time document ingestion
* Persistent memory storage
* Web interface using Streamlit

---

## Author

Developed as part of the Agentic AI Meeting Preparation Assistant assignment to demonstrate:

* Agentic AI
* Retrieval-Augmented Generation (RAG)
* Memory Management
* Tool Usage
* Multi-step Reasoning
