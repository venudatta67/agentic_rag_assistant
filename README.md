# Agentic RAG Assistant on AWS

## Project Overview

This project implements an **Agentic Retrieval-Augmented Generation (RAG) assistant**
grounded strictly in the official **AWS Retrieval-Augmented Generation Options guide**.

The system answers user questions by:
- Retrieving relevant content from the AWS guide
- Generating responses using only retrieved context
- Providing explicit citations
- Refusing to answer when information is not available

The design emphasizes:
- Zero hallucination
- Explainability
- Observability
- Reproducibility

---

## Architecture Diagram

                ┌───────────────┐
                │   User Query  │
                └───────┬───────┘
                        ↓
              ┌─────────────────────┐
              │ Planner / Router    │
              │ - Intent detection  │
              │ - Section routing   │
              └───────┬─────────────┘
                      ↓
              ┌─────────────────────┐
              │ Retrieval Agent     │
              │ - Vector search     │
              │ - Metadata filters │
              └───────┬─────────────┘
                      ↓
              ┌─────────────────────┐
              │ Synthesis Agent     │
              │ - Grounded answer  │
              │ - Citations        │
              └───────┬─────────────┘
                      ↓
              ┌─────────────────────┐
              │ Final Answer + Trace│
              └─────────────────────┘

---

## Agent Responsibilities

### Planner / Router Agent
- Analyzes user intent
- Classifies query type (definition, comparison, list, etc.)
- Identifies relevant AWS guide sections
- Determines single-pass or multi-pass retrieval strategy

### Retrieval Agent
- Performs semantic vector similarity search
- Applies section-based metadata filtering
- Returns ranked passages with confidence scores
- Supports multi-pass retrieval

### Synthesis / Answering Agent
- Combines retrieved passages into a coherent answer
- Ensures every claim is supported by context
- Attaches explicit citations (section name, page)
- Returns an explicit message when information is missing

---

## Setup Instructions

### Prerequisites
- Python 3.9+
- Virtual environment recommended

### Installation

pip install -r requirements.txt

---

## Environment Configuration

Create a .env file using .env.example and configure:
- Embedding model
- Vector database
- AWS region (if applicable)

---

## Document Ingestion

- Place the AWS guide PDF in the data/ directory.
- Run the ingestion pipeline:
  python main.py
  This performs:
    - PDF loading
    - Semantic chunking
    - Embedding generation
    - Vector index creation

---

## Running Queries

Once ingestion is complete, queries can be executed through the orchestration pipeline.
Example:
app.run("Compare fully managed RAG options with custom architectures")

The system will:
- Plan retrieval strategy
- Retrieve relevant passages
- Generate a grounded, cited answer

---

## Example Outputs

Query:
What are the retriever options on AWS?
Answer:
- Amazon Kendra – Managed enterprise search service
- Amazon OpenSearch Service – Search and analytics engine
- Amazon Aurora – Relational database option
- Amazon Neptune – Graph database
- Amazon MemoryDB – In-memory data store
(Sources: "Retrievers" section, AWS RAG guide)

---

## Limitations
- The system only answers questions covered in the AWS RAG guide
- No external web search or real-time data
- No inference beyond the provided document
- Designed for correctness and explain ability, not open-ended Q&A

