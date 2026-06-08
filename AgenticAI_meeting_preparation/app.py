import os
import ollama

from langchain_community.document_loaders import TextLoader
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter

# =====================================================
# EMBEDDINGS
# =====================================================

embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L4-v2"
)

# =====================================================
# LOAD DOCUMENTS
# =====================================================

client_docs = TextLoader(
    "data/clients/acme_profile.txt",
    encoding="utf-8"
).load()

meeting_docs = TextLoader(
    "data/meetings/acme_meeting_notes.txt",
    encoding="utf-8"
).load()

memory_docs = TextLoader(
    "data/memory/client_memory.txt",
    encoding="utf-8"
).load()

# =====================================================
# CHUNKING
# =====================================================

splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=50
)

client_chunks = splitter.split_documents(client_docs)
meeting_chunks = splitter.split_documents(meeting_docs)
memory_chunks = splitter.split_documents(memory_docs)

# =====================================================
# FAISS DATABASES
# =====================================================

CLIENT_DB = "faiss_client"
MEETING_DB = "faiss_meeting"
MEMORY_DB = "faiss_memory"

# ---------- CLIENT DB ----------

if os.path.exists(CLIENT_DB):
    client_db = FAISS.load_local(
        CLIENT_DB,
        embeddings,
        allow_dangerous_deserialization=True
    )
else:
    client_db = FAISS.from_documents(
        client_chunks,
        embeddings
    )
    client_db.save_local(CLIENT_DB)

# ---------- MEETING DB ----------

if os.path.exists(MEETING_DB):
    meeting_db = FAISS.load_local(
        MEETING_DB,
        embeddings,
        allow_dangerous_deserialization=True
    )
else:
    meeting_db = FAISS.from_documents(
        meeting_chunks,
        embeddings
    )
    meeting_db.save_local(MEETING_DB)

# ---------- MEMORY DB ----------

if os.path.exists(MEMORY_DB):
    memory_db = FAISS.load_local(
        MEMORY_DB,
        embeddings,
        allow_dangerous_deserialization=True
    )
else:
    memory_db = FAISS.from_documents(
        memory_chunks,
        embeddings
    )
    memory_db.save_local(MEMORY_DB)

# =====================================================
# SHORT TERM MEMORY
# =====================================================

conversation_history = []

# =====================================================
# TOOL 1
# =====================================================

def search_client_information(client_name):

    docs = client_db.similarity_search(
        client_name,
        k=3
    )

    return "\n".join(
        [doc.page_content for doc in docs]
    )

# =====================================================
# TOOL 2
# =====================================================

def retrieve_meeting_notes(client_name):

    docs = meeting_db.similarity_search(
        client_name,
        k=3
    )

    return "\n".join(
        [doc.page_content for doc in docs]
    )

# =====================================================
# TOOL 3
# =====================================================

def retrieve_long_term_memory(client_name):

    docs = memory_db.similarity_search(
        client_name,
        k=3
    )

    return "\n".join(
        [doc.page_content for doc in docs]
    )

# =====================================================
# AGENTIC WORKFLOW
# =====================================================

def prepare_meeting(client_name):

    print("\n[Tool] Retrieving Client Information...")
    client_info = search_client_information(
        client_name
    )

    print("[Tool] Retrieving Meeting Notes...")
    meeting_notes = retrieve_meeting_notes(
        client_name
    )

    print("[Tool] Retrieving Long-Term Memory...")
    memory = retrieve_long_term_memory(
        client_name
    )

    history_text = "\n".join(conversation_history[-5:])

    prompt = f"""
You are an AI Meeting Preparation Assistant.

Conversation History:
{history_text}

CLIENT PROFILE:
{client_info}

PREVIOUS MEETING NOTES:
{meeting_notes}

LONG TERM MEMORY:
{memory}

Analyze the retrieved information and generate a professional meeting brief.

Format:

=========================
MEETING BRIEF
=========================

Client:

Industry:

Business Challenges:

Previous Discussions:

Open Action Items:

Decision Makers:

Talking Points:

Next Best Actions:
"""

    response = ollama.chat(
        model="llama3",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response["message"]["content"]

# =================================================
