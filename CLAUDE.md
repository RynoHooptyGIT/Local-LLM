# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

A Python-based RAG (Retrieval-Augmented Generation) system using Ollama for local LLM inference and embeddings. The system ingests documents (PDFs, text), stores them as vector embeddings, and enables question-answering over the document corpus.

## Development Setup

```bash
# Activate virtual environment (already created)
source venv/bin/activate  # On macOS/Linux

# Install dependencies
pip install -r requirements.txt

# Ensure Ollama is running locally with required models:
ollama pull nomic-embed-text      # For embeddings
ollama pull deepseek-r1:8b        # For LLM responses (default)
```

## Architecture

### Core Components

**[vector_store.py](vector_store.py)** - Custom in-memory vector store
- `VectorStore` class using Ollama embeddings (nomic-embed-text by default)
- Implements cosine similarity search for document retrieval
- Stores documents, embeddings, and metadata in Python dictionaries
- Returns results in ChromaDB-compatible format (nested lists)
- Key methods: `add_documents()`, `search()`, `list_sources()`, `get_document()`

**[document_processor.py](document_processor.py)** - Text chunking utility
- `chunk_text()`: Splits text into overlapping chunks
- Default: 500 character chunks with 50 character overlap

**[document_ingestion.py](document_ingestion.py)** - Document ingestion pipeline
- `DocumentIngestion` class: Orchestrates PDF and text ingestion
- Uses PyPDF2 for PDF text extraction
- Chunks documents and adds them to the vector store with metadata (source, chunk_index, ingested_at)

**[rag_qa.py](rag_qa.py)** - RAG question-answering system
- `RAGQA` class: Retrieval-Augmented Generation interface
- Currently incomplete (contains TODOs for implementation)
- Intended to integrate vector store retrieval with Ollama LLM generation

### Data Flow

1. **Ingestion Pipeline**: PDF/text → extract text → chunk with overlap → generate embeddings via Ollama → store in VectorStore
2. **Query Pipeline**: Question → embed query → cosine similarity search → retrieve top N chunks → build prompt with context → LLM generates answer

### Important Implementation Details

- Vector store returns ChromaDB-compatible nested list format: `{"ids": [[...]], "documents": [[...]], "metadatas": [[...]], "distances": [[...]]}`
- Document IDs follow pattern: `{source_name}_chunk_{index}`
- Metadata includes: `source`, `chunk_index`, `ingested_at` (ISO format UTC)
- ChromaDB is installed but not actively used (custom VectorStore implementation instead)
