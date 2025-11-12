from PyPDF2 import PdfReader
from document_processor import chunk_text
from vector_store import VectorStore
from typing import List
import os
from datetime import datetime


class DocumentIngestion:
    """Handles ingestion of documents (PDF, text) into the vector store."""

    def __init__(self, vector_store: VectorStore):
        """
        Initialize the document ingestion system.

        Args:
            vector_store: VectorStore instance to store document chunks
        """
        self.vector_store = vector_store

    def ingest_pdf(self, pdf_path: str, chunk_size: int = 500, overlap: int = 50) -> int:
        """
        Ingest a PDF file into the vector store.

        Args:
            pdf_path: Path to the PDF file
            chunk_size: Size of each text chunk
            overlap: Overlap between chunks

        Returns:
            Number of chunks created and stored
        """
        #Check if file exists
        if not os.path.isfile(pdf_path):
            raise FileNotFoundError(f"PDF file not found: {pdf_path}")
        reader = PdfReader(pdf_path)

        #Extract text from all pages
        full_text = ""
        for page in reader.pages:
            full_text += page.extract_text()
        
        #get filename without path
        filename = os.path.basename(pdf_path)
        return self.ingest_text(full_text, filename, chunk_size, overlap)

    def ingest_text(self, text: str, source_name: str, chunk_size: int = 500, overlap: int = 50) -> int:
        """
        Ingest plain text into the vector store.

        Args:
            text: The text to ingest
            source_name: Name/identifier for the source
            chunk_size: Size of each text chunk
            overlap: Overlap between chunks

        Returns:
            Number of chunks created and stored
        """
        chunks = chunk_text(text, chunk_size, overlap)
        ids = [f"{source_name}_chunk_{i}" for i in range(len(chunks))]
        
        metadatas = [
            {
                "source": source_name,
                "chunk_index": i,
                "ingested_at": datetime.utcnow().isoformat()
            }
            for i in range(len(chunks))
        ]
        self.vector_store.add_documents(chunks, metadatas, ids)
        return len(chunks)
       
